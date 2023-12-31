FROM python:3.10-slim-bookworm
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ src/
COPY .env .env
CMD ["python", "src/main.py"]
