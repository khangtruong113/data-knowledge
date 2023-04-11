from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Read File")

# getOrCreate will get the conf or if not exist then it will create another conf
sc = SparkContext.getOrCreate(conf=conf)

text = sc.textFile("input.txt")

# this will trigger the step since before then it's lazy transofrmation
print(text.collect())

