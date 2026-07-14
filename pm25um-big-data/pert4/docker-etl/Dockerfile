# Gunakan base image Python 3.10 sesuai assignment
FROM python:3.10

# Install dependencies yang dibutuhkan: pymongo, requests, pandas
RUN pip install pymongo requests pandas

# Buat folder kerja di dalam container
WORKDIR /app

# Salin script ETL ke dalam container
COPY mongodb-openweather-api.py .

# Jalankan script saat container mulai
CMD ["python", "mongodb-openweather-api.py"]