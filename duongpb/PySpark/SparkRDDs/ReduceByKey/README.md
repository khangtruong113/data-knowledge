- Reduce by key is used to combined data base on Keys in RDD and then apply a reduce logic to them
- the data needs to be in this format
```commandline
(k,v), (k,v), (k2, v),.... : tuples
```
``````
example: ("Apple", 1), ("Ball", 1), ...
``````
- it creates new RDD
syntax: 
```commandline
rdd.reduceByKey(lambda x, y: x + y)
```
- this example above use a method like recursive
- reduceByKey can also be use to compare operator as well, not only boolean: 
- eg: 
```
# to show the min and max per course we do it like this flow:
# [course, mark] -> map[course, mark]
min_per_course = student_object.map(lambda x: [x[3], x[5]]).reduceByKey(lambda x, y: x if x < y else y)
min_per_course = student_object.map(lambda x: [x[3], x[5]]).reduceByKey(lambda x, y: x if x > y else y)
```
