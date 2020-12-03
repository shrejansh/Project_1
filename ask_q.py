from tkinter import *
# import tkinter.font as font
import pandas as pd
import os
import glob
from os import listdir
root=Tk()

result=[]

root.geometry('1000x800')

path=os.getcwdb()


print(path)
extension="csv"
os.chdir(path)
os.chdir("quiz_wise_questions")
result = glob.glob("*.csv")
print(result)



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
    heading.place_forget()
    for i in empty_l:
        i.place_forget()
    df=pd.read_csv("{}".format(quiz))
    def next_question(q):
    # takes user to next question
        q+=1
        if q==len(df.index):
            show_score()
        question.config(text="{}".format(df['question'].loc[q]))
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

    def score_calc():
        score=0
        for i in range(len(ans_dict)):
            if ans_dict[i]==df['correct_option'].loc[i]:
                score += df['marks_correct_ans'].loc[i]
            else:
                score += df['marks_wrong_ans'].loc[i]
        return score
        
    # question label
    question=Label(root,text="{}".format(df['question'].loc[0]),wraplength=400,bg="white")
    question.place(relx=0.5,rely=0.25,anchor="center")

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
    
    def show_score():
        question.place_forget()
        next_q.place_forget()
        for k in list_b:
            k.place_forget()
        statement=Label(root,text="Your score is {}".format(int(score_calc())))
        statement.place(relx=0.5,rely=0.5,anchor='center')
        
    # root.mainloop()
  
  

    
root.mainloop()