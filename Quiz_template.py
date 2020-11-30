import pandas as pd
import time
import sys
import threading



# ti=int(df.columns[-1][-3:-1])

def countdown(t):
    t=t*60
    while t:
        min=int(t/60)
        sec=int(t%60)
        timer = '{:50d}:{:<50d}'.format(min,sec)
        print(timer , end="\r")
        print(timer)
        t -= 1
        time.sleep(1)
    print("Thank u!")
    
# countdown(ti)
def run_quiz(q):
    df=pd.read_csv("P1 Quiz_via_CSV/quiz_wise_questions/q{}.csv".format(q))
    score = 0
    marked_choice=[]
    for i in range(len(df['question'])):
        # countdown(ti)
        print("\nQ.{} ".format(i+1)+df['question'].loc[i]+"\n"
                +"\n1. "+'{:30s}'.format(df['option1'].loc[i])
                +"2. "+'{:70s}'.format(df['option2'].loc[i])
                +"\n3. "+'{:30s}'.format(df['option3'].loc[i])
                +"4. "+'{:70s}'.format(df['option4'].loc[i])
                +"\n\n", end="\r")
        answer = int(input("Your Answer ->  "))
        marked_choice.append(answer)
        if answer == df['correct_option'].loc[i]:
            score += df['marks_correct_ans'].loc[i]
        else:
            score += df['marks_wrong_ans'].loc[i]
    print("you got", score, "out of", df['marks_correct_ans'].sum())
    return score

# t1=threading.Thread(target=countdown,args=[ti])
# t2=threading.Thread(target=run_quiz)

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# countdown(ti)        
# run_quiz(3)
