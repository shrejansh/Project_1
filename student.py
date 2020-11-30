class Student:
    
    def __init__(self,name,roll,password,whatsapp_no,quiz_no,marks):
        self.name=name
        self.roll=roll
        self.password=password
        self.whatsapp_no=whatsapp_no
        self.quiz_no=quiz_no
        self.marks=marks
        
    @classmethod
    def from_list(cls,stu_lis):
        name,roll,password,whatsapp_no,quiz_no,marks=stu_lis
        return cls(name,roll,password,whatsapp_no,quiz_no,marks)
        
    
    
        
# std_1[]
# std_1.quiz_p[3]=25
# print(len(std_1.quiz_p))