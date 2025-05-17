from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col, current_timestamp
import os
import requests
from bs4 import BeautifulSoup



def transform_data():
    # Step 1: Scrape oil news
    
    # Step 2: Start Spark session
    spark = SparkSession.builder \
        .appName("CommodityTransform") \
        .config("spark.jars.packages", "org.postgresql:postgresql:42.6.0") \
        .getOrCreate()

    # Step 3: EIA Data Transformation
    df = spark.read.option("multiline", "true").json("/tmp/raw_eia_data.json")
    df.printSchema()

    df_flat = df.select(explode(col("response.data")).alias("raw")) \
        .select(
            col("raw.period").alias("date"),
            col("raw.value").alias("price"),
            col("raw.series-description").alias("series_description"),
            col("raw.product-name").alias("product_name"),
            col("raw.area-name").alias("area_name"),
            col("raw.units").alias("units")
        )

    df_flat.write.mode("overwrite").parquet("/tmp/processed_eia_data")

    jdbc_url = "jdbc:postgresql://postgres:5432/airflow"
    jdbc_properties = {
        "user": "airflow",
        "password": "airflow",
        "driver": "org.postgresql.Driver"
    }

    df_flat.write.jdbc(url=jdbc_url, table="eia_processed_data", mode="overwrite", properties=jdbc_properties)
    print("✅ EIA data saved to PostgreSQL")

    # Step 4: News Data Transformation
    news_df = spark.read.text("/tmp/oil_news.txt").toDF("headline")
    news_df = news_df.withColumn("ingested_at", current_timestamp())

    news_df.write.jdbc(url=jdbc_url, table="oil_news", mode="overwrite", properties=jdbc_properties)
    print("✅ Oil news headlines saved to PostgreSQL")

    spark.stop()
