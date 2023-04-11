``` 
df.createGlobalTempView(name of the table)
df.createOrReplaceTempView(name of the table)
```

-> this transform this into a table in the session

```df = spark.sql("select * from Student")```

the same to 

```df.select(*).show()```