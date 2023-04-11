To convert DataFrame to RDD, we need to use this syntax: 

```commandline
rdd = df.rdd
rdd.filter(lambda x: x[1] == "male").collect()
```

after transforming, we can even provide the column name:
```commandline
rdd.filter(lambda x: x["age"] == 28).collect()
```

in case we need to have multiple grouping and continuous aggregation
, transforming from RDD to DF is a possible way, then we can conver them back 
