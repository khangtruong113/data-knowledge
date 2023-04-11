from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Read File")
# getOrCreate will get the conf or if not exist then it will create another conf
sc = SparkContext.getOrCreate(conf=conf)
# get the data from source
text = sc.textFile("input.txt")
print(text.collect())
def foo(x):
    # eg data : 1 2 3 then 4 5 6 8 then ...
    return_list = []
    # split to seperate characters
    for i in x.split(' '):
        # transform each character then transform them and finally add them to the return_list
        return_list.append(int(i) + 2)
    return return_list

transformed_rdd = text.map(foo)

print(transformed_rdd.collect())

