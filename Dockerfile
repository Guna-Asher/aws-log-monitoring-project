FROM python:3.11-slim

WORKDIR /app

COPY monitor.py .

RUN pip install boto3

CMD ["python", "monitor.py"]
