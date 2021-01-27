from flask import Flask, render_template, redirect, request, abort
from flask_sqlalchemy import SQLAlchemy
import uuid
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)



class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dist = db.Column(db.String(80), nullable=False)
    code = db.Column(db.String(120), nullable=False)
    count =  db.Column(db.Integer, nullable=False, default = 0)

    def __repr__(self):
        return '<Url %r>' % self.url


@app.route('/hello')
def hello():
   return "hello world"


@app.route('/')
def index():
    code = request.args.get('g', '')
    if code == '':
      return abort(404)
    url =  Url.query.filter_by(code=code).first()
    url.count = url.count + 1
    db.session.commit()
    if not url:
      return abort(404)
    return redirect(url.dist)

def generate_code(url):
  return uuid.uuid4().hex

@app.route('/shorten')
def shorten():
  url = request.args.get('url', '')
  code = generate_code(url)
  urlObj = Url(dist = url, code = code)
  db.session.add(urlObj);
  db.session.commit()
  return {'url': f'http://127.0.0.1:5000?g={code}'}


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 