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
columns = headers.split(',')
df = rdd.toDF(columns)

# filter by column
df.filter(df.course == "DB")

# df.filter(col("course") == "DB").show()

# multiple columns
df.filter((df.course == "DB") & (df.marks > 50))
course = ["DB", "Cloud", "OOP"]
# is in is to check filter for list
# is in
df.filter(df.course.isin(course))
# start with
df.filter(df.course.startswith("D"))
# contains
df.filter(df.name.contains("se"))
# like
df.filter(df.name.like("%se%")).show()