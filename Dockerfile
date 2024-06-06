FROM python:3.11.8-alpine
RUN apk add git
COPY requirements.txt manage.py run.py ./
COPY ./repo ./repo
COPY ./instance ./instance
COPY ./static ./static
ENV SECRET_KEY xxx
ENV GITHUB_CLIENT_ID xxx
ENV GITHUB_CLIENT_SECRET xxx
RUN pip install -r requirements.txt && python manage.py db init && python manage.py db migrate && python manage.py db upgrade
CMD ["python", "run.py"]  