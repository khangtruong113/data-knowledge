# import all libraries needed for this project
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, udf, col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("Spark Dataframe").getOrCreate()

df = spark.read.options(inferSchema='True', header='True').csv("OfficeDataProject.csv")
headers = df.first()

# print the total number of employees in the company
employee_number = df.count()

# - print the total number of departments in the comp
department_number = df.dropDuplicates(["department"]).count()

#- print the department names of the comp
department_names = df.dropDuplicates(["department"]).select((["department"]))

# - print the total number of employees in each department
number_of_emp_department = df.groupBy("department").count().withColumnRenamed("count", "number_of_emp")

# - print the total number of employee in each state
number_of_emp_state = df.groupBy(df.state).count()

# - print the total number of employees in each state in each department
number_of_emp_state = df.groupBy(df.state, df.department).count()

# - print the mini and max salaries in each department and sort salaries in ASC
min_salary = df.groupBy("department").min("salary").withColumnRenamed("min(salary)", "min").sort("min")
max_salary = df.groupBy("department").max("salary").withColumnRenamed('max(salary)', 'max').sort("max")

# - print the name of employees working in NY state under Finance department whose
# bonuses are greater than the avg bonuses of employee in NY
avg_bonus = df.filter(df.state == "NY").groupBy("state").agg(avg("bonus")).withColumnRenamed("avg(bonus)", "avg_bonus").select("avg_bonus").collect()[0]['avg_bonus']
emp_avg = df.filter((df.state == "NY") & (df.department == "Finance") & (df.bonus > avg_bonus))

# - raise salaries $500 of all employees whose age > 45
# we will create a UDF taking age and salary
def incr_salary(age, salary):
    if age > 45:
        return salary + 500
    return salary

incrSalaryUDF = udf(lambda x, y: incr_salary(x, y), IntegerType())

incr_salary = df.withColumn("salary", incrSalaryUDF(col("age"), col("salary")))

# - create DF of all those employees whose age is >45 and save them in a file

df_age = df.filter(df.age > 45).write.csv("output")