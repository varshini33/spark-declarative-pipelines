from pyspark import pipelines as dp
import pyspark.sql.functions as F

SOURCE_PATH = "s3://goodcabs-hamz/data-store/trips"


# https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/schema
#dp.table creates a streaming table
@dp.table(
    name="transportation.bronze.trips",
    comment="Streaming ingestion of raw orders data with Auto Loader",
    table_properties={
        "quality": "bronze",
        "layer": "bronze",
        "source_format": "csv",
        "delta.enableChangeDataFeed": "true",
        "delta.autoOptimize.optimizeWrite": "true",
        "delta.autoOptimize.autoCompact": "true",
    },
)
def orders_bronze():
    df = (
        spark.readStream.format("cloudFiles") #autoloader defined with readStream and cloudFiles
        .option("cloudFiles.format", "csv")
        .option("cloudFiles.inferColumnTypes", "true")
        .option("cloudFiles.schemaEvolutionMode", "rescue") # for new rescue columns if there is a schema changes
        .option("cloudFiles.maxFilesPerTrigger", 100) # max files processed in one batch
        .load(SOURCE_PATH)
    )

     # Rename the problematic column
    df = df.withColumnRenamed(
        "distance_travelled(km)", # () in column names are a problem
        "distance_travelled_km"
    )

    df = df.withColumn("file_name", F.col("_metadata.file_path")).withColumn("ingest_datetime", F.current_timestamp())

    return df
