from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Read File")
# getOrCreate will get the conf or if not exist then it will create another conf
sc = SparkContext.getOrCreate(conf=conf)
# get the data from source
text = sc.textFile("input.txt")

transformed_rdd = text.filter(lambda x: x == '4 5 6 8')

print(transformed_rdd.collect())

