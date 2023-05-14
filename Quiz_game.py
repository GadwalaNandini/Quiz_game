# Quiz_game


questions=("Which symbol is used in python to represent comment",
           "Which one is NOT a legal Variable in python ",
           "How do you create a variable with the floating number 1.6",)     # add as many question you can
options=(("A. /","B. @","C. #"),
          ("A. _myvar","B. My-var","C. my_var"),
           ("A. x=1.6","B. x=int(1.6)","C. x=type(1.6)"))
answers=(("C"),("B"),("A"))
guesses=[]
score=0            
question_num=0

for question in questions:
    print("---------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
      score = score+1
      print("CORRECT")
    else:
      print("INNCORRECT")
      print(f"{answers[question_num]} is the correct answer! ")

    question_num=question_num+1

print("---------------------------------------")
print("----------        Results   -----------")
print("---------------------------------------")

print("answers: ",end=" ")
for answer in answers:
  print(answer,end=" ")
print()


print("guesses: ",end=" ")
for guess in guesses:
  print(guess,end=" ")
print()

score= score/len(questions)*100
print(f"Your Score is : {score}%")
