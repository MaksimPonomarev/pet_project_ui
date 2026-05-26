FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install --with-deps chromium

COPY . .

CMD ["pytest", "-s", "-v", "--reruns=2", "--reruns-delay=3"]