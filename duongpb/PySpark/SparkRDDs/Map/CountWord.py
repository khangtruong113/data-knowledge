# description: In this excercise we get the data from the fike wordinput.txt,
# then count each number in each word then output the result

from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Read File")
# getOrCreate will get the conf or if not exist then it will create another conf
sc = SparkContext.getOrCreate(conf=conf)
# get the data from source
text = sc.textFile("wordinput.txt")
def count_word(sentence: str):
    # eg data : 1 2 3 then 4 5 6 8 then ...
    return_list = []
    # split to seperate characters
    for word in sentence.split(' '):
        # transform each character then transform them and finally add them to the return_list
        return_list.append(len(word))
    return return_list

count_function = text.map(count_word)

# lambda way
count_lambda = text.map(lambda x: [len(s) for s in x.split(' ')])

print(count_lambda.collect())

print(count_function.collect())