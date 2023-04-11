### normal grouping
help DF to create a group of data so that we can aggregate later on
syntax: 

```commandline
df.groupBy("gender")
```
###### note that after grouping, you need to perform an aggregate or transformation for the data 
so we need to apply aggregation and it should be something like this: 
```commandline
df.groupBy("gender").sum("marks").show()
or
df.groupBy("course").count().show()
or
df.groupBy("age").avg("marks").show()
```

### multiple Grouping
the grouping of multiple fields will happen with the exact number and by the order of the fields

for example: 
```commandline
df.groupBy("course").count().show()
```

This code will group by all the course, then once again group by the gender, then count for each group
so we will have the following group: 

| course | gender | count 
|--------|--------|-------|
| math   | female | 50    |
| math   | male   | 50    |
| literature | female | 20 |
| literature | male | 20|

### multiple aggregation
```commandline
from pyspark.sql.functions import sum, avg, max, min, mean, count
```

then we have these line of code

```commandline
df.groupBy("course").agg(count("*"), sum("marks"))
```

###### note that it's safer to use the col("column_name") after aggregation because it will take the column of the transformed table, not the original table, which will be called if we use dataframe.column_name

