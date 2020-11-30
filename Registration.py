from student import Student
from test import insert_student,insert_marks,find_stu
import sqlite3


print("Please login\n")
roll=str(input("Enter your username\n"))
password=str(input("Enter your password\n"))
if find_stu(roll,password):
    print("You are not registered yet \nPlease register for the quiz\n")
    name=str(input("What is your name?\n"))
    roll=str(input("Enter your roll no\n"))
    password=str(input("Enter your password\n"))
    whatsapp_no=int(input("Enter whatsapp no?\n"))

# quiz={1:23}



# std_1=Student(name,roll,password,whatsapp_no,quiz)
# insert_marks(std_1)
# insert_student(std_1)