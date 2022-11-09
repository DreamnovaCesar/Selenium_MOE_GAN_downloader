FROM python:3.9.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./Selenium_Class_main.py"]
