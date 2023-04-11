#### explanation

This section code is to illustrate how can we apply a function on map()

First, create a spark context, then we transform the data through all these steps: 
1. get data from input.txt
2. map the data with the foo() function, this function handle these steps:
- split all characters by the space (' ')
- each character then cast to number and then + 2 to them
- these character then added to a returned list

run the job by using this command:

```set PYSPARK_PYTHON=python```

```
spark-submit MapFunction.py
```