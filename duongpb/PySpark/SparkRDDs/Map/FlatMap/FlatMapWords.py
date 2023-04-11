# description: In this excercise we get the data from the fike wordinput.txt,
# then count each number in each word then output the result

from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Read File")
# getOrCreate will get the conf or if not exist then it will create another conf
sc = SparkContext.getOrCreate(conf=conf)
# get the data from source

text = sc.textFile("wordinput.txt")

flat_map_count = text.flatMap(lambda x: x.split(' '))
print(flat_map_count.collect())