- Group by key is used to create groups based on Keys in RDD
- the data needs to be in this format
```commandline
(k,v), (k,v), (k2, v),.... : tuples
```
- it creates new RDD
syntax: 
```commandline
rdd.groupByKey()
```
mapValue(list) are usually used to get the group data
where the one inside the () is the data type that we want to display the value

To run the job in example, use this command:
```set PYSPARK_PYTHON=python```

```
spark-submit GroupByKey.py
```