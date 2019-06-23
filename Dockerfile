FROM python:3.6-alpine
RUN apk add git
COPY requirements.txt manage.py run.py ./
COPY ./repo ./repo
RUN pip install -r requirements.txt && python manage.py db init && python manage.py db migrate && python manage.py db upgrade
CMD ["python", "run.py"]  