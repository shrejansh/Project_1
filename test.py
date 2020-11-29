import sqlite3
from student import Student

conn=sqlite3.connect('project1_quiz_cs384.db')
c=conn.cursor()
c.execute("""CREATE TABLE project1_registration(
                name text,
                roll text,
                password blob,
                whatsapp_no real
            )""")

c.execute("""CREATE TABLE project1_marks(
                roll text,
                quiz_num integer,
                total_marks integer
            )""")

def insert_student(stu):
    with conn:
        c.execute("INSERT INTO project1_registration VALUES (:name,:roll,:password,:whatsapp_no)",{'name':stu.name,'roll':stu.roll,'password':stu.password,'whatsapp_no':stu.whatsapp_no})

def insert_marks(stu):
    with conn:
        c.execute("INSERT INTO project1_marks VALUES (:roll,:quiz_no,:total_marks)",{'roll':stu.roll,})