from tkinter import *
import tkinter.font as font
# from quiz_template import countdown
from PIL import ImageTk,Image
import time
import pandas as pd

df=pd.read_csv("q{}.csv".format(1))

root=Tk()

root.geometry('1000x800')
 
  # Countdown function  
def countdown(t):
    mins=int(t/60)
    sec=int(t%60)
    timer = '{:50d}:{:<50d}'.format(mins,sec)
    myLabel1.config(text="{}".format(timer))
    t-=1
    myLabel1.after(1000,lambda:countdown(t))
    
myLabel1=Label(root,text="20:00")
myLabel1.place(relx=0.9,rely=0.1,anchor="center")
myLabel1.after(1000,lambda:countdown(20*60-1))

def next_question(q):
    # takes user to next question
    q+=1
    question.config(text="{}".format(df['question'].loc[q]))
    option1.config(text="{}".format(df['option1'].loc[q]),bg="white",command=lambda:choose(option1,1,q))
    option2.config(text="{}".format(df['option2'].loc[q]),bg="white",command=lambda:choose(option2,2,q))
    option3.config(text="{}".format(df['option3'].loc[q]),bg="white",command=lambda:choose(option3,3,q))
    option4.config(text="{}".format(df['option4'].loc[q]),bg="white",command=lambda:choose(option4,4,q))
    next_q.config(command=lambda:next_question(q))

l=dict()
def choose(o,num,q):
    
    # changes background color of chosen option
    
    l[q]=num
    print(list_b-{o})
    for i in list_b:
        i.config(bg="white")
    o.config(bg="red") 
    list_b.add(o) 
    pass

def score_calc():
    score=0
    for i in range(len(df.index)):
        if l[i]==df['correct_option'].loc[i]:
            score += df['marks_correct_ans'].loc[i]
        else:
            score += df['marks_wrong_ans'].loc[i]
    return score

# question label
question=Label(root,text="{}".format(df['question'].loc[0]),bg="white")
question.place(relx=0.5,rely=0.5,anchor="center")

# option button
option1=Button(root,text="{}".format(df['option1'].loc[0]),command=lambda:choose(option1,1,0))
option1.place(relx=0.2,rely=0.8,anchor="sw")  
option2=Button(root,text="{}".format(df['option2'].loc[0]),command=lambda:choose(option2,2,0))
option2.place(relx=0.8,rely=0.8,anchor="sw")  
option3=Button(root,text="{}".format(df['option3'].loc[0]),command=lambda:choose(option3,3,0))
option3.place(relx=0.2,rely=0.85,anchor="sw")  
option4=Button(root,text="{}".format(df['option4'].loc[0]),command=lambda:choose(option4,4,0))
option4.place(relx=0.8,rely=0.85,anchor="sw")  
 
list_b={option1,option2,option3,option4}
#next button   
next_q=Button(root,text="NEXT",command=lambda:next_question(0))  
next_q.place(relx=0.5,rely=0.9,anchor="center")

root.mainloop()
print(int(score_calc()))
# print(font.families())