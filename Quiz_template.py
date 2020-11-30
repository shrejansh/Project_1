import pandas as pd

df=pd.read_csv("P1 Quiz_via_CSV/quiz_wise_questions/q1.csv")

def run_quiz():
    score = 0
    for i in range(len(df['question'])):
        answer = int(input("\n"+df['question'].loc[i] +"\n" + df['option1'].loc[i]+"\n"+df['option2'].loc[i]+"\n"+df['option3'].loc[i]+"\n"+ df['option4'].loc[i]+"\n\n"+"Your Answer ->"))
        if answer == df['correct_option'].loc[i]:
            score += df['marks_correct_ans'].loc[i]
        else:
            score += df['marks_wrong_ans'].loc[i]
    print("you got", score, "out of", df['marks_correct_ans'].sum())
        
run_quiz()