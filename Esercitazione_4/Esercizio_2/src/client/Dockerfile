FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api api
COPY template template

EXPOSE 8000

CMD ["uvicorn", "api.html_server:app", "--host", "0.0.0.0", "--port", "8000"]

