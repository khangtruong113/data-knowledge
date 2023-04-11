## Concept
- RDD is transformation step, it stands for Resilient Distributed Dataset
- RDD is immutable collection of object and contain data, think of it like a 
bus stop on the way to deliver data to the final destication
- Spark distributes the data in RDD to different node across 
the cluster and process this in parallel
- sparks only trigger the dataflow when there's action

### these are the overview for all Spark RDDs features:
- count(): to count all records number
- distint() : select distint and unique record
- filter(boolean or value): to filter the records we want
- groupByKey(k,v): group the record by their key, value will be wrap
- map(value): to apply an action or a function over every each elements of the RDDs
- partition: change, increase or delete the number of the RDDs partitions
- reduceBykey(k, v -> k, v are 2 incremental elements): reduce the elements by their key, apply the logic to reduce
- saveAsTextFile: save the result as folder or files, for folder, it will return 1 file for each partitions)
- max, min, avg: operator apply for RDDs
- groupBy("name of the key"): group elements by the name of their key