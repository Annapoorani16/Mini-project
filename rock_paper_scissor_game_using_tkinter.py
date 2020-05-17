import random
import tkinter as tk
window=tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game")
window.configure(background='black')
pic1=tk.PhotoImage(file="rock.png")
pic2=tk.PhotoImage(file="paper.png")
pic3=tk.PhotoImage(file="scissor.png")
USER_SCORE = 0
COMP_SCORE = 0
a=["rock","paper","scissor"]
def result(user_choice,comp_choice):
   global USER_SCORE
   global COMP_SCORE
   if(comp_choice==user_choice):
       result="Tie"
   elif((comp_choice=="rock" and user_choice=="paper")or(comp_choice=="paper" and user_choice=="scissor")or (comp_choice=="scissor" and user_choice=="rock")):
       result="You won"
       USER_SCORE += 1
   else:
       result="You Lose"
       COMP_SCORE += 1
   text_area = tk.Text(master=window,height=10,width=40,bg="red")
   text_area.grid(column=0,row=4)
   answer = "Result:{rs} \nYour Choice: {uc} \nComputer's Choice : {cc} \nYour Score : {u} \nComputer Score : {c} ".format(rs=result,uc=user_choice,cc=comp_choice,u=USER_SCORE,c=COMP_SCORE)
   text_area.insert(tk.END,answer)
def rock():
    global user_choice
    global comp_choice
    user_choice = 'rock'
    comp_choice= random.choice(a)
    result(user_choice,comp_choice)
def paper():
    global user_choice
    global comp_choice
    user_choice = 'paper'
    comp_choice= random.choice(a)
    result(user_choice,comp_choice)
def scissor():
    global user_choice
    global comp_choice
    user_choice = 'scissor'
    comp_choice = random.choice(a)
    result(user_choice, comp_choice)
btn1=tk.Button(window,image=pic1,command=rock).grid(row=0,column=1)
btn2=tk.Button(window,image=pic2,command=paper).grid(row=0,column=2)
btn3=tk.Button(window,image=pic3,command=scissor).grid(row=0,column=3)
window.mainloop()

