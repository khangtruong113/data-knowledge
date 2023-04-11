we can write the dataframe to a place and a location
syntax : 

```commandline
df.write.options(header='True').csv('location')
```

this is to save the data at a specific location

we  can then read the data of the file from the location

```commandline
df = spark.read.csv(the location we just extract data to)
```

Mode for writting: 
``````overwrite``````: overwrite the old data with the new one

``````append`````` : append new data beneath every file

``````ignore``````: ignore the data writing if there's already file

``````error`````` : raise exception if the data already exist