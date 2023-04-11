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

# selecting
dfRdd.select("gender", "name").show()

dfRdd.select(dfRdd.name, dfRdd.email).show()

from pyspark.sql.functions import col, lit
dfRdd.select(col("roll"), col("name")).show()

# select all
dfRdd.select("*").show()

# select from column position
dfRdd.select(dfRdd.columns[2:6]).show()

dfRdd.select(dfRdd.columns[2:3], "marks", col("email"))

#with Column
# this is to manipulate and change column data type, this will return a new DF
# the old DF is not effecting cause it's immutable
dfRdd = dfRdd.withColumn("roll", col("roll").cast("String"))

# manipulate data, note that the first attribute is the name of the newly created
# and if the name of the column doesnt match any old column, a new column will be created
dfRdd = dfRdd.withColumn("marks", col("marks") + 20)

# lit is for applying all value to a new or old column
dfRdd = dfRdd.withColumn(("Country", lit("USA")))

# if we have multiple withColumn, the value will follow the number of transformation, not
    # from the original column
dfRdd.withColumn("marks", col("marks") -10 ).withColumn("update mark", col("marks") + 20).show()

# rename Column
df = dfRdd.withColumnRenamed("gender", "sex")

# we can alias the column name just for selecting or view the data
df.select(col("name").alias("Full name")).show()
