both sort and order by are use to organize the data 
after an order.
syntax: 
```commandline
df.sort(df.column_name.asc(), df.column_name.desc(),...).show()
df.sort("column_name",...)
```
by default the sort will be in the ASC order

```commandline
df.orderBy(df.column_name.asc(), df.column_name.desc(),...)
```
by default the order by will be in the ASC order