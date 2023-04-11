# import the data type to single column so we can provide the schema for spark datafram later on
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("Spark Dataframe").getOrCreate()
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("RDD")
sc = SparkContext.getOrCreate(conf=conf)

text = sc.textFile(('StudentData.csv'))
headers = text.first()
rdd = text.filter(lambda x: x != headers).map(lambda x: x.split(','))

print(rdd.collect())
# creating the DF with header base on the header we just create
# it apply the headers to every column of it
# note that we need sparkContext to use toDF
columns = headers.split(',')
dfRdd = rdd.toDF(columns)
dfRdd.show()
dfRdd.printSchema()

# creating DF from RDD with our own created schema
schema = StructType(
    [
        StructField("age", IntegerType(), True), # true mean this column can have a null value
        StructField("gender", StringType(), True),
        StructField("name", StringType(), True),
        StructField("course", StringType(), True),
        StructField("roll", StringType(), True),
        StructField("marks", IntegerType(), True),
        StructField("email", StringType(), True)
    ]
)
# note that we need to cast the data into the schema we use to create the DF
dfRdd2 = spark.createDataFrame(rdd, schema=schema)
dfRdd2.printSchema()