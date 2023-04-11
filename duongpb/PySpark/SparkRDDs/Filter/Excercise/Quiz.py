from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Read File")
# getOrCreate will get the conf or if not exist then it will create another conf
sc = SparkContext.getOrCreate(conf=conf)
# get the data from source
text = sc.textFile("input.txt")

flat_word = text.flatMap(lambda x: x.split(' ')).filter(lambda x: x[0] == "a" or x[0] == "c")

print(flat_word.collect())