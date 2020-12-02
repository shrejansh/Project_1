from tkinter import *
import tkinter.font as font
import pandas as pd
import os
import glob

root=Tk()
frame=Frame(root)
frame.grid(row=0,column=0)

frame1=Frame(root)
frame.grid(row=0,column=0)

frame2=Frame(root)
frame2.grid(row=1,column=1)
root.geometry('1000x800')

path=os.getcwd()
# path = 'c:\\Users\Shreyansh\
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))

heading=Label(frame,text="Which quiz would you like to take??",padx=10,pady=10)
heading.grid(row=0,column=0)
for i in range(len(result)):
    button = Button(frame2, text=result[i],command=lambda:read_c(result[i],heading))
    button.grid(row=i+2,column=1)
# print(result)

button=Button(frame1,text="Yada Yada")


def read_c(q,f):
    f.tkraise()
    df=pd.read_csv("{}".format(q))
    
root.mainloop()