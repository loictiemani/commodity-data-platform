
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
- **Storage in Parquet Format**

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

---

## 📂 Project Structure

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
```

---

## 🚀 Getting Started

### 1. Clone & Install
```bash
git clone https://github.com/yourusername/commodity-data-platform.git
cd commodity-data-platform
pip install -r requirements.txt
```

### 2. Run Docker Environment
```bash
docker-compose up --build
```

- Airflow UI: http://localhost:8080  
- Spark UI: http://localhost:8081  
- FastAPI: http://localhost:8000/commodities/oil

### 3. Trigger the DAG

Visit [Airflow UI](http://localhost:8080), enable and run `commodity_data_pipeline`.

---

## 🧪 Sample API Output

```json
GET /commodities/oil

[
  { "date": "2024-05-01", "price": 78.52 },
  { "date": "2024-04-30", "price": 77.83 }
]
```

---

## ✅ Data Validation with Great Expectations

Great Expectations runs automatically in the DAG to ensure:

- Price is within expected range
- Nulls are not present
- Columns are not missing

Use the expectation suite under `src/validation/`.

---

## 📚 Key Learnings

- Modular, testable, and scalable pipeline design
- Real-time data ingestion and validation
- CI/CD pipeline for reliable deployments
- Hands-on integration of Spark, Airflow, and FastAPI

---

## 👤 Author

**Loic**  
Data Engineer | Asset & Analytics Specialist  
_This project simulates real-world responsibilities in a commodity trading context like Glencore._

---

## 📝 License

MIT License – use freely with attribution.
