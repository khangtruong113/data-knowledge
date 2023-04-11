the option is for customizing the df creation
example 

```df2 = spark.read.option("header", True).csv('StudentData.csv')```

spark can and have the option to infer schema and also we can set multiple options for the pineline
there's also a parameter in the options which is delimeter='something' to say that we want to split
the file and read it with the delimiter as the filled in value