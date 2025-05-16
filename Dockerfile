# Base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy files
COPY ./src /app

# Install dependencies

COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install python-dotenv


COPY . .

    # Expose API port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
