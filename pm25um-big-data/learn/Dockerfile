# Use Python 3.10 as base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Install system dependencies (optional but recommended)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy ETL script into container
COPY mongodb-openweather-etl.py .

# Create a non-root user for security
RUN useradd -m -u 1000 etluser && chown -R etluser:etluser /app
USER etluser

# Default command - run the ETL script
CMD ["python", "mongodb-openweather-etl.py"]