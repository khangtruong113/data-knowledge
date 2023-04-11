dbutils.fs.rm("table Location", True)

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Spark Streaming DF").getOrCreate()
word = spark.readStream.text("table location")
display(word) #display the word out to console

print(word.groupBy("value").count()...)

word.writeStream.format("console").outputMode("complete").start()

# output mode is to mark that it's complete'

# aggregate

