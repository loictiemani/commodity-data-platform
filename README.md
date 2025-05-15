# 🛢️ Commodity Data Platform

A simulated data engineering platform for commodity trading analytics, inspired by a real-world Glencore use case. This project demonstrates end-to-end ingestion, transformation, validation, and API delivery of commodity market data using modern tools like Airflow, Spark, FastAPI, and Great Expectations.

---

## 📊 Use Case

Designed to support trading analysts by delivering clean, transformed, and validated data from external sources (EIA API, web news scraping). The project includes:

- **Batch Ingestion** from APIs and websites
- **Spark-based Transformation** and optimization
- **Automated Data Validation** using Great Expectations
- **API Layer** with FastAPI
- **Workflow Orchestration** with Apache Airflow
- **CI/CD** using GitHub Actions
- **Containerized Setup** with Docker Compose

---

## ⚙️ Tech Stack

| Layer            | Technology                      |
|------------------|----------------------------------|
| Orchestration    | Apache Airflow                  |
| Ingestion        | Python, Requests, BeautifulSoup |
| Processing       | Apache Spark (PySpark)          |
| Validation       | Great Expectations              |
| Serving          | FastAPI                         |
| CI/CD            | GitHub Actions                  |
| Infrastructure   | Docker Compose                  |
| Storage Format   | Parquet                         |

---

## 🧱 Architecture Diagram

```mermaid
graph TD
    A[External APIs: EIA, News Web] --> B[Airflow DAGs]
    B --> C[Ingestion Scripts]
    C --> D[Spark Transformations]
    D --> E[Processed Data (Parquet)]
    E --> F[FastAPI Service]
    E --> G[Great Expectations Validation]
    F --> H[Consumers: Trading Analysts]
```

commodity-data-platform/
├── dags/                      # Airflow DAGs
├── src/
│   ├── ingestion/             # Data ingestion (API + Web scraping)
│   ├── transformation/        # Spark-based transformation
│   ├── validation/            # Great Expectations checks
│   └── api/                   # FastAPI endpoints
├── tests/                     # Unit tests
├── notebooks/                 # EDA and testing
├── .github/workflows/         # CI/CD pipeline
├── docker-compose.yml         # Local dev environment
├── Dockerfile                 # For API or batch jobs
├── requirements.txt
└── README.md
