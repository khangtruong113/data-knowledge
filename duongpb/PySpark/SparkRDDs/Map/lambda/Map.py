from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Read File")

# getOrCreate will get the conf or if not exist then it will create another conf
sc = SparkContext.getOrCreate(conf=conf)

text = sc.textFile("input.txt")
print(text.collect())
# this will trigger the step since before then it's lazy transofrmation
text_transform = text.map(lambda x: x.split(' '))

print(text_transform.collect())
