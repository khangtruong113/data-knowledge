allow to count for all the elements from a DF

using 
```commandline
count()
```

we can also drop all duplication by 
```commandline
dropDuplicates([name of the column])
multiple columns: 
dropDuplicates(["gender", "name"])
```

Distinct
```commandline
df.select("gender", "age").distinct()
```