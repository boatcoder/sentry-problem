Clone this repo,
create and activate a venv
```
pip install -r requirements.txt
export SENTRY_DSN=value from the sentry dashboard
export DJANGO_DEBUG=0
python manage.py migrate
python manage.py runserver

curl http://localhost:8000/
```

Should log to sentry, but does not
