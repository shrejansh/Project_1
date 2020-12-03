import sqlite3 
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import *
from tkinter.constants import FLAT
import os
import pandas as pd

con=sqlite3.connect("project1_quiz_cs384.db")
c=con.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS project1_registration (
    name TEXT NOT NULL,
    roll TEXT NOT NULL,
    password TEXT NOT NULL,
    whatsappnumber INTEGER
    )""")
result=[]
path=os.path.join(os.getcwd(),"quiz_wise_questions")
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".csv"):
             result.append( file)
def next():
    he.pack_forget()
    a11.pack_forget()
    a12.pack_forget()
    b11.pack_forget()
    b12.pack_forget()
    c11.pack_forget()
    c12.pack_forget()
    d11.pack_forget()
    d12.pack_forget()
    regbtn1.pack_forget()
    logbtn1.pack_forget()

    head.pack()
    head2.pack()
    a.pack(fill='x')
    a1.pack(fill='x',padx=50,ipadx=10,ipady=7)
    b.pack(fill='x',pady=(30,0))
    b1.pack(padx=50,ipadx=10,ipady=7)
    logbtn.pack(pady=10)
    regbtn.pack(pady=10,padx=10)

def sel_quiz(name,roll):
    # width = root.winfo_screenmmwidth()
    n=tk.Label(root,text=f"Name : {name} Roll : {roll}",font=" 20 ",bg="#ADD8E6")
    n.place(relx=0.5,rely=0.1,anchor="center",relwidth = 1.0)
    heading=Label(root,text="Which quiz would you like to take??",padx=10,pady=10)
    heading.place(relx=0.5,rely=0.2,anchor="center")
    empty_l=[]
    for i in range(len(result)):
        button = Button(root,  height=2, width=8,text=result[i],command=lambda i=i: read_c(result[i]))
        button.place(relx=0.5,rely=0.4+float(i+1)/10,anchor="center")
        empty_l.append(button)
    # print(result)
 
    def read_c(quiz):
        # f.tkraise()
        def countdown(t):
            mins=int(t/60)
            sec=int(t%60)
            timer = '{:50d}:{:<50d}'.format(mins,sec)
            myLabel1.config(text="{}".format(timer))
            t-=1
            myLabel1.after(1000,lambda:countdown(t))
            
        myLabel1=Label(root,text="20:00",bg="#90ee90")
        myLabel1.place(relx=0.5,rely=0.03,anchor="center",relwidth=.9)
        myLabel1.after(1000,lambda:countdown(20*60-1))


        heading.place_forget()
        for i in empty_l:
            i.place_forget()
        df=pd.read_csv("quiz_wise_questions/{}".format(quiz))
        def next_question(q):
        # takes user to next question
            q+=1
            if q==len(df.index):
                show_score()
            question.config(text="{}".format(df['question'].loc[q]))
            correct.config(text="Correct answer : {}".format(df['marks_correct_ans'].loc[q]))
            negative.config(text="Wrong answer : {}".format(df['marks_wrong_ans'].loc[q]))
            comp.config(text="Compulsory : {}".format(df['compulsory'].loc[q]))
            
            option1.config(text="{}".format(df['option1'].loc[q]),bg="white",command=lambda:choose(option1,1,q))
            option2.config(text="{}".format(df['option2'].loc[q]),bg="white",command=lambda:choose(option2,2,q))
            option3.config(text="{}".format(df['option3'].loc[q]),bg="white",command=lambda:choose(option3,3,q))
            option4.config(text="{}".format(df['option4'].loc[q]),bg="white",command=lambda:choose(option4,4,q))
            next_q.config(command=lambda:next_question(q))
            

        ans_dict=dict()
        def choose(o,num,q):      
            # changes background color of chosen option
            ans_dict[q]=num
            for i in list_b:
                i.config(bg="white")
            o.config(bg="red") 
            pass
        
        correct_ch=0
        wrong_ch=0
        attempted=[]
        def score_calc():
            score=0
            global correct_ch
            global wrong_ch
            correct_ch=0
            wrong_ch=0
            # print(ans_dict)
            for i in ans_dict:
                
                attempted.append(i)
                if ans_dict[i]==df['correct_option'].loc[i]:
                    score += df['marks_correct_ans'].loc[i]
                    correct_ch+=1
                else:
                    score += df['marks_wrong_ans'].loc[i]
                    wrong_ch+=1
            unattempted=set([i for i in range(len(df.index))])-set(attempted)
            # print(unattempted)
            for k in unattempted:
                if df['compulsory'].loc[k]=='y':
                    score+=df['marks_wrong_ans'].loc[k]
            return score
           
        # question label
        question=Label(root,text="{}".format(df['question'].loc[0]),wraplength=400,bg="white")
        question.place(relx=0.5,rely=0.25,anchor="center")
        
        # Correct ans Negative and Compulsory
        correct=Label(root,text="Correct answer : {}".format(df['marks_correct_ans'].loc[0]),wraplength=400,bg="white")
        correct.place(relx=0.75,rely=0.3,anchor="center")
        negative=Label(root,text="Wrong answer : {}".format(df['marks_wrong_ans'].loc[0]),wraplength=400,bg="white")
        negative.place(relx=0.75,rely=0.35,anchor="center")
        comp=Label(root,text="Compulsory : {}".format(df['compulsory'].loc[0]),wraplength=400,bg="white")
        comp.place(relx=0.75,rely=0.4,anchor="center")
        top_labels=[question,correct,negative,comp]

        # option button
        option1=Button(root,text="{}".format(df['option1'].loc[0]),command=lambda:choose(option1,1,0))
        option1.place(relx=0.3,rely=0.5,anchor="center")  
        option2=Button(root,text="{}".format(df['option2'].loc[0]),command=lambda:choose(option2,2,0))
        option2.place(relx=0.7,rely=0.5,anchor="center")  
        option3=Button(root,text="{}".format(df['option3'].loc[0]),command=lambda:choose(option3,3,0))
        option3.place(relx=0.3,rely=0.6,anchor="center")  
        option4=Button(root,text="{}".format(df['option4'].loc[0]),command=lambda:choose(option4,4,0))
        option4.place(relx=0.7,rely=0.6,anchor="center")  
        
        list_b=[option1,option2,option3,option4]
        
        #next button   
        next_q=Button(root,text="NEXT",command=lambda:next_question(0))  
        next_q.place(relx=0.5,rely=0.8,anchor="center")
        
        print("This ->>",correct_ch,wrong_ch)
        def show_score():
            for i in top_labels:
                i.place_forget()
            next_q.place_forget()
            submit_b.place_forget()
            myLabel1.place_forget()
            for k in list_b:
                k.place_forget()
            # print(correct_ch)
            statement=Label(root,text=f"Total questions : {len(df.index)} \n Total questions attempted : {correct_ch+wrong_ch} \n Total correct questions : {correct_ch} \nTotal wrong questions : {wrong_ch} \n Your score is {int(score_calc())} out of {df['marks_correct_ans'].sum()}")
            statement.place(relx=0.5,rely=0.5,anchor='center')   
            # statement2=Label(root,text="Attempted questions : {}".format(len(ans_dict)))
            # statement2.place(relx=0.5,rely=0.65,anchor='center')   
            # export_response()
            # statement=Label(root,text="Your score is {}".format(int(score_calc())))
            # statement.place(relx=0.5,rely=0.5,anchor='center') 
         
        
        # submit button
        submit_b=Button(root,text="SUBMIT",command=show_score)
        submit_b.place(relx=0.8,rely=0.8,anchor="center")
        
        # exporting to csv
        def export_response(event):
            legend=['Correct Choice','Wrong choice','Unattempted','Marks Obtained','Total Quiz Marks']
            total=[correct_ch,wrong_ch,len(df['question'])-(correct_ch+wrong_ch),int(score_calc()),df['marks_correct_ans'].sum()]
            # t={"Legend":legend,"Total":total}
            df['Marked Choice']=None
            df['Legend']=None
            df['Total']=None
            for i in ans_dict:
                df['Marked Choice'].loc[i]=ans_dict[i]
            for i in range(5):
                df['Legend'].loc[i]=legend[i]
                df['Total'].loc[i]=total[i]
            df.to_csv(f'quiz_wise_responses/{quiz[:-4]}_{roll}.csv',index=False)
            # print(df.to_string())
            
        root.bind('<Control_L><Alt_L><e>',export_response) 
        # root.bind('<Control_R><Alt_R><e>',export_response) 
        
    
            



        
            
def login():
    user=a1.get(),
    password=b1.get()
    c.execute("SELECT * FROM project1_registration WHERE roll=(?)",(user))

    if len(c.fetchall())==0:
       msg.showwarning(title="No data found", message="please register")
    else :
        c.execute("SELECT * FROM project1_registration WHERE roll=(?)",(user))
        l=list(c.fetchone())
        if l[2]==password:
            print("succes login")
            head.pack_forget()
            head2.pack_forget()
            a.pack_forget()
            a1.pack_forget()
            b.pack_forget()
            b1.pack_forget()
            regbtn.pack_forget()
            logbtn.pack_forget()
            sel_quiz(l[0],user)

        else :
            msg.showwarning(title="Invalid", message="please use valid password and username")



def login1():
    name=a12.get()
    roll=b12.get()
    password=c12.get()
    what_num=d12.get()
    c.execute("INSERT INTO project1_registration VALUES (?,?,?,?)",(name,roll,password,what_num))
    con.commit()
    
    he.pack_forget()
    a11.pack_forget()
    a12.pack_forget()
    b11.pack_forget()
    b12.pack_forget()
    c11.pack_forget()
    c12.pack_forget()
    d11.pack_forget()
    d12.pack_forget()
    regbtn1.pack_forget()
    logbtn1.pack_forget()

    sel_quiz(name,roll)

    


    
def reg():
    head.pack_forget()
    head2.pack_forget()
    a.pack_forget()
    a1.pack_forget()
    b.pack_forget()
    b1.pack_forget()
    regbtn.pack_forget()
    logbtn.pack_forget()
    global he,a11,a12,b11,b12,c11,c12,d11,d12,logbtn1,regbtn1

    he=tk.Label(root, text="Registration", font="comicsansms 30 bold",fg="blue", pady=15)
    he.pack()

    a11 = tk.Label(root ,text = "Name",font=" 20 ",padx=(100))
    a11.pack(fill='x')

    a12 = tk.Entry(root,width=400,)
    a12.pack(fill='x',padx=50,ipadx=10,ipady=7)

    b11 = tk.Label(root ,text = " Roll",font=" 20 ",padx=(100))
    b11.pack(fill='x',pady=(30,0))

    b12 = tk.Entry(root,width=400,)
    b12.pack(padx=50,ipadx=10,ipady=7)

    c11 = tk.Label(root ,text = " Password",font=" 20 ",padx=(100))
    c11.pack(fill='x',pady=(30,0))

    c12 = tk.Entry(root,width=400,)
    c12.pack(padx=50,ipadx=10,ipady=7)

    d11 = tk.Label(root ,text = " Whatsapp Number",font=" 20 ",padx=(100))
    d11.pack(fill='x',pady=(30,0))

    d12 = tk.Entry(root,width=400,)
    d12.pack(padx=50,ipadx=10,ipady=7)

    logbtn1 = tk.Button(root,text="Register and login",command = login1,background="green",font=" 18 ",padx=20,pady=5,)
    logbtn1.pack(pady=10)

    regbtn1 = tk.Button(root,text="login",command = next,background="red",font=" 18 ",padx=30,pady=5,)
    regbtn1.pack(pady=10,padx=10)

    


# main geometry  
root=tk.Tk()
root.geometry("700x600") 
root.minsize(600,600)
root.maxsize(1500,900) 
root.title('quiz')


# landing page
head=tk.Label(root, text="QUIZ", font="comicsansms 30 bold",fg="blue", pady=15)
head.pack()

head2=tk.Label(root, text="login", font="comicsansms 24 bold", pady=15)
head2.pack()

a = tk.Label(root ,text = "username",font=" 20 ",padx=(100))
a.pack(fill='x')

a1 = tk.Entry(root,width=400)
a1.pack(fill='x',padx=50,ipadx=10,ipady=7)

b = tk.Label(root ,text = " password",font=" 20 ",padx=(100))
b.pack(fill='x',pady=(30,0))

b1 = tk.Entry(root,width=400,show="* ")
b1.pack(padx=50,ipadx=10,ipady=7)

logbtn = tk.Button(root,text="login",command = login,background="green",font=" 18 ",padx=20,pady=5,)
logbtn.pack(pady=10)

regbtn = tk.Button(root,text="Register",command = reg,background="red",font=" 18 ",padx=30,pady=5,)
regbtn.pack(pady=10,padx=10)


# driver code
if __name__=="__main__":

    root.mainloop()
    con.close()
    