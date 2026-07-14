from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Read HDFS Example") \
    .master("local[*]") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://namenode:9000") \
    .getOrCreate()

df = spark.read.csv("/linkedin-data/linkedin_job_postings.csv", header=True)

df.show(5)

df.printSchema()