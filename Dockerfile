FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
COPY start.sh .
COPY app.py .
COPY scripts/ ./scripts/
COPY frontend/ ./frontend/
COPY logs/ ./logs/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    chmod +x start.sh
EXPOSE 8989
CMD ["bash", "start.sh"]
