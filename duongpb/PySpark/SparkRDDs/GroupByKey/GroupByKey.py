from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Read File")
# getOrCreate will get the conf or if not exist then it will create another conf
sc = SparkContext.getOrCreate(conf=conf)
# get the data from source
text = sc.textFile("input.txt")
print(text)

# transform the data to tuple in order to group them by key
tuple_data = text.flatMap(lambda x: x.split(' ')).map(lambda x: (x,len(x)))

# group the data by their key and then display the value in list format
group_data = tuple_data.groupByKey().mapValues(list)
print(group_data.collect())