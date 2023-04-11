### FlatMap

- Flat map is used as a maper of data and explodes data before final output
- it create a new RDD, this also can be apply with a function or lambda
- syntax: 
```commandline
rdd.flatMap(lambda x:x.split())
```
- flatmap will apply map into 1 level lower as it will flatten everything into
1 unified type of elements