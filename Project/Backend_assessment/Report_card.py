import pandas as pd

courses = pd.read_csv('courses.csv')
students = pd.read_csv('students.csv')
tests = pd.read_csv('tests.csv')
marks = pd.read_csv('marks.csv')

Student_information = {}
ls = len(courses)
id = 1
for i in courses['id']:
    print(i)
    print(courses['1'])


# Student_information[id]