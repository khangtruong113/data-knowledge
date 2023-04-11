Default we have 2 partitions for each RDD
- create new RDD
- syntax to reduce the number of partitions: 
```commandline
rdd.coalesce(number_of_partitions)
```
- syntax to increase or change the number of partitions:
```commandline
rdd.repartition(number_of_partitions)
```

to check the rdd partition we use : 
```commandline
rdd.getNumPartitions()
```