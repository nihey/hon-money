# Hon Backend

Backend provides minimum data via a REST API. It is built with [Flask RESTful](https://flask-restful.readthedocs.org/en/0.3.2/)
with [Storm](https://storm.canonical.com/).

## Dependencies

You will have to install dependencies via pip with:

```
$ pip install -r requirements.txt // or
```

Be warned, psycopg might fail for depending on libpq-dev (you could install it
via APT)

## Running

* `make server`
* Data will be served from http://localhost:8090.
