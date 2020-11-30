from student import Student
from test import insert_student,insert_marks,find_stu,get_registered
import sqlite3
from quiz_template import run_quiz


print("Please login\n")
roll=str(input("Enter your username\n"))
password=str(input("Enter your password\n"))
if not find_stu(roll,password):
    print("You are not registered yet \nPlease register for the quiz\n")
    name=str(input("What is your name?\n"))
    roll=str(input("Enter your roll no\n"))
    password=str(input("Enter your password\n"))
    whatsapp_no=int(input("Enter whatsapp no?\n"))
    std_1=Student(name,roll,password,whatsapp_no,0,0)
    insert_student(std_1)
else:
    l=list(get_registered(roll))
    l.append(0)
    l.append(0)
    std_1=Student.from_list(l)
quiz_no=int(input("Which quiz do you want to take?"))
run_quiz(quiz_no)
std_1.quiz_no=quiz_no
std_1.marks=int(run_quiz(quiz_no))



# std_1=Student(name,roll,password,whatsapp_no,quiz)
insert_marks(std_1)
# insert_student(std_1)