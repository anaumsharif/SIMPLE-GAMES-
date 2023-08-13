# GUESS GAME : 
# GUESS A NUMBER 
from random import randint 
random_number = randint(0,100)
#  OPTIONAL : print(random_number)
x = -1
while x != random_number:
    if x != -1:
        print("WRONG GUESS \n     BETTER LUCK NEXT TIME ! ")
    x = input("Enter a number : ")
    x = int(x)
print("     YOU GUESSED CORRECTLY")