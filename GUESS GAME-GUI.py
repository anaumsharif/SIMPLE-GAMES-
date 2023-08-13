from random import randint
from tkinter import *
from tkinter import simpledialog,messagebox

main = Tk()
main.withdraw()

random_number=randint(0,100)
print(random_number)

x=-1
while x!= random_number:
    if x!= -1:
        messagebox.showinfo("Wrong","Incorrect Guess")

    x = simpledialog.askstring("Guess","Enter a Number:")
    x = int(x)
    
    if x==random_number:
        messagebox.showinfo("Right","YOU GUESSED CORRECTLY")
        exit()
main.mainloop()