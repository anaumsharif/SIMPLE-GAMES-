from tkinter import *
from tkinter import simpledialog,messagebox

main = Tk()
main.withdraw()

questions = ["What is the capital of India ?",
             "Who is the presisdent of US ?",
             "What is the National bird of India ?",
             "What is the capital of France  ?",
             "What is the capital of Spain  ?"   
            ]
answer = [ "Delhi",
          "Biden",
          "Peacock",
          "Paris",
          "Madrid"]

score = 0
# applying loop and matching the index of the answers of the user with the correct answer  
for i in range (0,len(questions)):
    print(questions[i])
    user_answer = simpledialog.askstring(questions[i],"Answer :")
    # user_answer = user_answer.lower()
    if user_answer == answer[i]:
        messagebox.showinfo("CORRECT ANSWER" , "WELL DONE ")
        score = score + 1
    else :
        messagebox.showinfo("INCORRECT ANSWER ")
messagebox.showinfo("YOUR SCORE =", str(score))
