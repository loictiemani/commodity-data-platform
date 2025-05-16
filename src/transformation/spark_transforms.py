from pyspark.sql import SparkSession

def transform_data():
    spark = SparkSession.builder.appName("CommodityTransform").getOrCreate()
    df =spark.read.json("/tmp/raw_eia_data.json")
    df_flat = df.selectExpr("explode(series.data) as raw") \
                .selectExpr("raw[0] as date", "raw[1] as price")
    
    df_flat.write.mode("overwrite").parquet("/tmp/processed_eia_data")
    print("✅ Data transformed and saved")