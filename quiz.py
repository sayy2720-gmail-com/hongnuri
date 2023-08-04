BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = '#3E497A'
BTN_COLOR = "#F0F0F0"

import csv
from tkinter import *
from tkinter import messagebox
import random

with open("test1.csv", "r", encoding="UTF-8-sig") as file:
    questions = list(csv.reader(file))

answer = 0
question_count = 0

#문제 생성
def next_question():
    global answer, question_count

    # 문제가 15개를 초과하면 종료
    if question_count >= 15:
        messagebox.showinfo("게임 종료", "모든 문제를 풀었습니다!")
        return
    
    for i in range(4):
        buttons[i].config(bg=BTN_COLOR)

    multi_choice = random.sample(questions,4)
    answer = random.randint(0,3)
    cur_question = multi_choice[answer][0]

    question_label.config(text=cur_question)

    for i in range(4):
        buttons[i].config(text=multi_choice[i][1])
        
    question_count += 1

#정답체크
def check_answer(idx):
    idx = int(idx)
    if answer == idx:
        buttons[idx].config(bg=CORRECT_COLOR)
        messagebox.showinfo("정답", "정답입니다!!")
        window.after(1000, next_question)
    else:
        buttons[idx].config(bg=WRONG_COLOR)




window = Tk()
window.title("영어 퀴즈")
window.config(padx=30, pady=10, bg=BGCOLOR)

question_label = Label(window, width=55, height=2, text="test",
                        font=("나눔바른펜", 11, "bold"), bg=BGCOLOR, fg="white")
question_label.pack(pady=30)

buttons = []
for i in range(4):
    btn = Button(window, text=f"{i}번", width=35, height=2, font=("나눔바른펜", 15, "bold"),
                 bg=BTN_COLOR, command =lambda idx=i: check_answer(idx))
    btn.pack()
    buttons.append(btn)


next_btn = Button(window, text="다음문제", width=15, height=2,
                  command=next_question,
                  font=("나눔바른펜", 15, "bold"), bg=CORRECT_COLOR)
next_btn.pack(pady=30)

next_question()

window.mainloop()
