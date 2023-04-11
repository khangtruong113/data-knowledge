from pyspark.sql import SparkSession

# we can only have 1 spark session at the time
spark = SparkSession.builder.appName("Spark Dataframe").getOrCreate()

# the option is for customizing the df creation
# df2 = spark.read.option("header", True).csv('StudentData.csv')
# spark can and have the option to infer schema and also we can set multiple options for the pineline
# there's also a parameter in the options which is delimeter='something' to say that we want to split
# the file and read it with the delimeter as the filled in value
df2 = spark.read.options(inferSchema='True', header='True').csv('StudentData.csv')
df2.printSchema()
