from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col
import os

def transform_data():
    spark = SparkSession.builder.appName("CommodityTransform").config("spark.jars.packages", "org.postgresql:postgresql:42.6.0").getOrCreate()

    # Read raw JSON
    df = spark.read.option("multiline", "true").json("/tmp/raw_eia_data.json")

    # Print schema for debugging
    df.printSchema()

    # Explode the 'data' array inside 'response'
    df_flat = df.select(explode(col("response.data")).alias("raw")) \
                .select(
                    col("raw.period").alias("date"),
                    col("raw.value").alias("price"),
                    col("raw.series-description").alias("series_description"),
                    col("raw.product-name").alias("product_name"),
                    col("raw.area-name").alias("area_name"),
                    col("raw.units").alias("units")
                )

    # Write transformed data as Parquet (for local backup/debugging)
    df_flat.write.mode("overwrite").parquet("/tmp/processed_eia_data")

    # JDBC connection values from your .env setup
    jdbc_url = "jdbc:postgresql://postgres:5432/airflow"
    jdbc_properties = {
        "user": "airflow",
        "password": "airflow",
        "driver": "org.postgresql.Driver"
    }

    # Write to PostgreSQL
    df_flat.write \
        .jdbc(url=jdbc_url, table="eia_processed_data", mode="overwrite", properties=jdbc_properties)

    print("✅ Data transformed and saved to both Parquet and PostgreSQL")

    spark.stop()
