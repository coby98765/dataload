FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


ENV DB_URL="John Doe"
ENV DB_USER="root"
ENV DB_PASS=""

EXPOSE 8000

CMD ["python", "services/data_loader.py"]