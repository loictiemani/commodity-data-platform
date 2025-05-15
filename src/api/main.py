from fastapi import FastAPI
from pathlib import Path
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"status": "FastAPI is live!"}

@app.get("/data")
def get_data():
    file_path = Path("data/processed/example.parquet")
    if not file_path.exists():
        return {"error": "File not found."}
    df = pd.read_parquet(file_path)
    return df.head(10).to_dict(orient="records")
