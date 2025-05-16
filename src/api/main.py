from fastapi import FastAPI
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

DATA_PATH = Path(os.getenv("DATA_DIR", "data/processed")) / "example.parquet"

@app.get("/")
def root():
    return {"status": "FastAPI is live!"}

@app.get("/data")
def get_data():
    if not DATA_PATH.exists():
        return {"error": "File not found."}
    df = pd.read_parquet(DATA_PATH)
    return df.head(10).to_dict(orient="records")
