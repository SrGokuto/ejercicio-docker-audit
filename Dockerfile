FROM python:3.14-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip uninstall -y setuptools wheel

COPY . /app

EXPOSE 5050
CMD ["python", "app.py"]