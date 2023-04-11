In this example, we run a simple spark job in the file SimpleSample.py

to run the spark job, you can simple run the file with the python command:

- 1st way:

```cd <this_dir>```

```python SimpleSample.py```

- 2nd way: 

you can trigger the job by summiting the job through hadoop and then run it with cluster

###### Do this to point your spark python to your using python
```set PYSPARK_PYTHON=python```

```spark-submit SimpleSample.py```

