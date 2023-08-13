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
# answers could be :
# answer = [ "delhi",
        #   "biden",
        #   "peacock",
        #   "paris",
        #   "madrid"]
score = 0
# applying loop and matching the index of the answers of the user with the correct answer  
for i in range (0,len(questions)):
    print(questions[i])
    user_answer = input("Answer :")
    # user_answer = user_answer.lower()
    if user_answer == answer[i]:
        print("CORRECT ANSWER , WELL DONE ")
        score = score + 1
    else :
        print("INCORRECT ANSWER ")
print(f"YOUR SCORE = {score}")

# However there is an error if the user input isn't correctly formatted that is if the first letter of the word isn't capital it ives incorrect answer 
# so it can be solved by feeding the answer in lower case and the user input can be coverted into lower case by using the function .lower() so tthe input matches correctly 