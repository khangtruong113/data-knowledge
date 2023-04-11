import re

from pyspark import SparkConf, SparkContext

# regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

conf = SparkConf().setAppName("Mini project")

sc = SparkContext.getOrCreate(conf=conf)

text = sc.textFile("StudentData.csv")
header = text.first()
student_line = text.filter(lambda x: x != header)
# adding validation and split into list
student_object = student_line.map(lambda line: line.split(',')).filter(lambda x: len(x) == 7)
    # .filter(lambda x: re.fullmatch(regex, x[6]))

print('total number: ' + str(student_object.count()))
# tuple_object = student_object.map(lambda student: [["age", student[0]],
#                                                    ["gender", student[1]], ["name", student[2],
#                                                    ["course", student[3]], ["roll", student[4]],
#                                                    ["marks", student[5]], ["email", student[6]]]])

############################################################################################################################################################################################
# Show the number of student in file
num_of_students = student_object.count()

############################################################################################################################################################################################
student_by_gender = student_object.map(lambda x: [x[1], x[5]]).reduceByKey(lambda x,y: int(x)+int(y))

############################################################################################################################################################################################
# show the total number of students that have passed or failed, 50+ marks are require to pass the course
# print(student_object.collect())
number_pass_student = student_object.filter(lambda x: int(x[5]) > 50).count()
number_fail_student = student_object.filter(lambda x: int(x[5]) < 50).count()
#
# print("fail student number : " + str(number_fail_student))
# print("pass student number : " + str(number_pass_student))

############################################################################################################################################################################################
# show the total number of students enrolled per course
# creating index for each student for the course they enroll
number_of_enroll_per_course = student_object.map(lambda x: [x[3], 1]).reduceByKey(lambda x, y: x+y)

############################################################################################################################################################################################
# show the avg marks that students have achieved per course
# to explain for this, first we make key,value like this : [course name, [marks, index]] => [course name, [mark1 + mark2, index1 + index 2] => [course name, [total mark/total index]
avg_per_course = student_object.map(lambda x: [x[3], [x[5], 1]]).reduceByKey(lambda x, y: [int(x[0]) + int(y[0]), int(x[1]) + int(y[1])]).map(lambda x: [x[0], x[1][0]/x[1][1]])
avg_per_course = student_object.groupBy("")

############################################################################################################################################################################################
# show the min and max marks per course
# to show the min and max per course we do it like this flow:
# [course, mark] -> map[course, mark]
min_per_course = student_object.map(lambda x: [x[3], x[5]]).reduceByKey(lambda x, y: x if x < y else y)
min_per_course = student_object.map(lambda x: [x[3], x[5]]).reduceByKey(lambda x, y: x if x > y else y)

############################################################################################################################################################################################
# show the avg of age of female and male students
# we need to have the transformation as followed: [gender, [age, index]] => [gender, [total age, total index]] => [gender, [avg]]
avg_age = student_object.map(lambda x: [x[1], [x[0], 1]]).reduceByKey(lambda x, y: [int(x[0]) + int(y[0]), int(x[1]) + int(y[1])])\
    .map(lambda x: [x[0], x[1][0]/x[1][1]])


