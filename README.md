### shorten url

how to run
create virtualenv and install requirement

```
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```

create database

```
  flask shell
  from app import db
  db.create_all()
```

run application

```
  python3 app.py
```

provided api

| endpoint           | result                |
| :----------------- | :-------------------- |
| /shorten?url=[url] | shorturl for this url |
| shorturl           | send to the url       |

the app count every time request sended to shorturl

the app have no url validation so if you gave uncorrect url and try to use the shorturl it will send you to the same uncorrect url
