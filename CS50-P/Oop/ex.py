#this is the example of how to use OOP as a libraries
from student_classmethod import Student
s = Student("Bidyut", "Gryffindor")
print(s)

std = Student.get()
print(std)

from hat import Hat
Hat.sort("Ron")