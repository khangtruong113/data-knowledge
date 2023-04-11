SaveAsTextFile is the method to extract the file out of a RDD

A job can be seperate into different partition and then output the result
if we dont extract the file out then it will create as many files as the number of clusters we have

we can check the number of partition by using 
rdd.getNumPartitions()

default are 2 partitions

