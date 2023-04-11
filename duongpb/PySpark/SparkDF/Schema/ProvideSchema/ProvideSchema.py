# import the data type to single column so we can provide the schema for spark datafram later on
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql import SparkSession

# we can only have 1 spark session at the time
spark = SparkSession.builder.appName("Spark Dataframe").getOrCreate()
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
df = spark.read.schema(schema).csv("StudentData.csv")

# the option is for customizing the df creation
# df2 = spark.read.option("header", True).csv('StudentData.csv')
# spark can and have the option to infer schema and also we can set multiple options for the pineline
# there's also a parameter in the options which is delimeter='something' to say that we want to split
# the file and read it with the delimeter as the filled in value
df.printSchema()

