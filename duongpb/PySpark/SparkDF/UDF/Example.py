# this is an example for UDF

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
df= rdd.toDF(columns)
def get_total_salary(salary: int, bonus: int):
    return salary + bonus

# this function that takes x and y from 2 column and then return the result of the function with schema as Integer Type
total_salary_UDF = udf(lambda x,y: get_total_salary(x,y ), IntegerType())

df.withColumn("total_salary", total_salary_UDF(df.salary, df.bonus)).show()