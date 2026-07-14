# PM25UM Big Data - Medicine Data ETL Pipeline

> Proyek Big Data untuk pemrosesan data obat (medicine data) menggunakan Apache Spark, MongoDB, dan Data Lake Architecture.

---

## Mata Kuliah

**Big Data** - Program Studi Sistem Informasi

### Dosen Pengampu

| Nama | GitHub |
|------|--------|
| M. Zainal Arifin, S.Kom., M.Kom. | - |
| Dewi Oktaviani, S.Kom., M.Kom. | [@oktavianidewi](https://github.com/oktavianidewi) |

---

## Overview

Proyek ini mendemonstrasikan pipeline big data end-to-end untuk data obat, mulai dari ekstraksi data dari MongoDB, pemrosesan dengan Spark, penyimpanan di Data Lake, hingga visualisasi di Power BI.

### Fitur Utama

- **ETL Pipeline** - Extract, Transform, Load data obat dari MongoDB
- **Data Lake Architecture** - Implementasi raw, cleaned, dan gold layers
- **Apache Spark** - Pemrosesan data skala besar dengan PySpark
- **Power BI Dashboard** - Visualisasi dan analisis data obat
- **Docker Deployment** - Containerisasi aplikasi dengan Docker
- **MapReduce** - Pemrosesan data terdistribusi

## Tech Stack

| Teknologi | Kegunaan |
|-----------|----------|
| Apache Spark (PySpark) | Pemrosesan data skala besar |
| MongoDB | Database sumber |
| Delta Lake | Format data lake |
| Docker & Docker Compose | Containerisasi |
| HDFS | Distributed file system |
| Power BI | Visualisasi & dashboard |
| Python | Bahasa pemrograman utama |

## Project Structure

```
pm25um-big-data-main/
├── data_lake/                    # Data Lake (raw → cleaned)
│   ├── raw/                      # Data mentah dari MongoDB
│   └── cleaned/                  # Data yang sudah dibersihkan
├── data_mart/                    # Data Mart (gold layer)
│   └── gold/                     # Data siap analisis
├── spark_data_lake/              # Spark-based Data Lake
│   ├── bronze/                   # Data mentah (Parquet)
│   ├── silver/                   # Data bersih (Parquet)
│   └── gold/                     # Data analytics (JSON)
├── powerbi_data/                 # Data untuk Power BI
├── etl_output/                   # Output hasil ETL
├── pm25um-big-data/              # Sub-proyek
│   ├── app/                      # Aplikasi utama (MapReduce, PySpark)
│   ├── sandbox/                  # Eksperimen & testing
│   ├── infra/                    # Infrastructure (Docker, HDFS)
│   ├── pertemuan4/               # Materi pertemuan 4
│   └── learn/                    # Materi pembelajaran
├── docker-hello-world/           # Contoh Docker deployment
├── Medicine_ETL_Spark.ipynb      # Notebook utama ETL
├── UTS_BIGDATA.ipynb             # Notebook UTS
├── mongodb-openweather-api.ipynb # Integrasi MongoDB + Weather API
├── RAG.ipynb                     # Retrieval-Augmented Generation
└── PowerBI_Import_Guide.txt      # Panduan Power BI
```

## Getting Started

### Prerequisites

- Python 3.8+
- MongoDB
- Apache Spark
- Docker & Docker Compose (optional)
- Power BI Desktop (optional)

### Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/username/pm25um-big-data-main.git
   cd pm25um-big-data-main
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup environment variables**
   ```bash
   # Copy .env template
   cp pm25um-big-data/learn/.env.example pm25um-big-data/learn/.env
   
   # Edit .env with your API keys
   OPENWEATHER_API_KEY=your_api_key_here
   CITY=surabaya
   ```

4. **Start MongoDB**
   ```bash
   # Using Docker
   docker run -d -p 27017:27017 --name mongodb mongo:latest
   ```

5. **Run ETL Pipeline**
   ```bash
   # Open Jupyter Notebook
   jupyter notebook Medicine_ETL_Spark.ipynb
   ```

## Data Sources

| Deskripsi | Jumlah |
|-----------|--------|
| Total transaksi penggunaan obat | 2,000 |
| Katalog obat unik | 1,000 |
| Rumah sakit | 20 |
| Kategori obat | 5 |
| Rentang data | 365 hari |

### Kategori Obat

1. Analgesic (Pereda nyeri)
2. Antibiotic (Antibiotik)
3. Antiviral (Antivirus)
4. Vitamin
5. Supplement (Suplemen)

## Power BI Dashboard

Tersedia 7 file CSV untuk visualisasi di Power BI:

| File | Deskripsi |
|------|-----------|
| `medicine_main_table.csv` | Tabel utama (recommended) |
| `medicine_details.csv` | Master data obat |
| `medicine_usage.csv` | Data penggunaan obat |
| `category_analytics.csv` | Analisis per kategori |
| `monthly_trends.csv` | Trend penggunaan bulanan |
| `top_medicines.csv` | Top 20 obat terpopuler |
| `hospital_analytics.csv` | Analisis per rumah sakit |

### Import ke Power BI

1. Buka Power BI Desktop
2. Home → Get Data → Text/CSV
3. Pilih file `medicine_main_table.csv`
4. Klik Load untuk import data
5. Buat visualisasi sesuai kebutuhan

Lihat `PowerBI_Import_Guide.txt` untuk panduan lengkap.

## Docker Deployment

```bash
# Build and run containers
docker-compose up -d

# Stop containers
docker-compose down
```

## MapReduce

Contoh implementasi MapReduce untuk pemrosesan data:

```bash
# Run mapper
python pm25um-big-data/app/mapper.py < input.txt

# Run reducer
python pm25um-big-data/app/reducer.py < mapper_output.txt
```

## Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Apache Spark Documentation
- MongoDB University
- Power BI Community
- Docker Documentation

---

**Note**: Pastikan untuk tidak commit API keys atau credentials ke repository. Gunakan environment variables atau `.env` files yang sudah di-gitignore.
