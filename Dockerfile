FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONPATH=/app
ENV OPENAI_API_KEY=dummy
ENV SERPAPI_API_KEY=dummy
ENV USE_MOCKS=true

CMD ["python", "scripts/run_researcher.py", "--prd", "data/prd_example.md"]
