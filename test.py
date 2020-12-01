import sqlite3
from student import Student


conn=sqlite3.connect('project1_quiz_cs384.db')
c=conn.cursor()
# c.execute("""CREATE TABLE project1_registration(
#                 name text,
#                 roll text,
#                 password blob,
#                 whatsapp_no real
#             )""")

# c.execute("""CREATE TABLE project1_marks(
#                 roll text,
#                 quiz_num integer,
#                 total_marks integer
#             )""")

def check_quiz(roll,quiz_no):
    c.execute("SELECT * FROM project1_marks WHERE roll=? AND quiz_num=?",(roll,quiz_no))
    b=c.fetchone()
    if b:
        c.execute("DELETE FROM project1_marks WHERE roll=? AND quiz_num=?",(roll,quiz_no))
    pass
        
    
    
def get_registered(roll):
    c.execute("SELECT * FROM project1_registration WHERE roll=?",(roll,))
    return c.fetchone()
    
def find_stu(roll,password):
    c.execute("SELECT * FROM project1_registration WHERE roll=?",(roll,))
    a=c.fetchall()
    c.execute("SELECT * FROM project1_registration WHERE password=?",(password,))
    b=c.fetchall()
    return len(a)*len(b)

def insert_student(stu):
    with conn:
        c.execute("INSERT INTO project1_registration VALUES (:name,:roll,:password,:whatsapp_no)",{'name':stu.name,'roll':stu.roll,'password':stu.password,'whatsapp_no':stu.whatsapp_no})

def insert_marks(stu):
    with conn:
        c.execute("INSERT INTO project1_marks VALUES (:roll,:quiz_no,:total_marks)",{'roll':stu.roll,'quiz_no':stu.quiz_no,'total_marks':stu.marks})

# std_1=Student('Shreyansh','1801zz32','moron',8738299822,{1:23,2:45})
# insert_student(std_1)
# insert_marks(std_1)
c.execute("SELECT * FROM project1_marks")
print(c.fetchall())
# print(get_registered('1801zz32'))
# print(check_quiz('kale',1))