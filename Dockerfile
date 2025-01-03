FROM python:3.12.7-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN chmod 755 django.sh

EXPOSE 8888

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]

# entrypoint to run the django.sh file
ENTRYPOINT ["/app/django.sh"]