questions = (("How many numbers are there in the alphabet")
           ,("What is the sound that a cow makes?"),
           ("What color is the sky?"),
           ("What is 2 + 2?"),
           ("What color is a leaf?"))

options = (("A. 26", "B. 25", "C. 24", "D. 23" ),
           ("A. wow","B. hi","C. greetings","D. moo"),
           ("A. yellow,", "B. Orange", "C. Black", "D. Blue"),
           ("A. 3", "B. 6", "C. 5", "D. 4"),
           ("A. green", "B. pink", "C. white", "D. brown"))

letter_choice = ("A","B","C","D")
answers = ("A","D","D","D","A")
userChoice = True
currQuestion = ""

guesses = []
score = 0
question_num = 0


for question in questions:
    print("------------------------------")
    print(question)
    currQuestion = question
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    print(guess)

    
    if guess == "A":
        userChoice = True
            
    elif guess == "B": 
        userChoice = True

    elif guess =="C":
        userChoice = True

    elif guess =="D":
        userChoice = True
    else:
        userChoice = False

    while userChoice == False:
        print(f"{guess} is not a choice. Choose option A,B,C,D")
        print(currQuestion)
        for option in options[question_num]:
            print(option)
        guess = input("Enter (A,B,C,D): ").upper()
        if guess == "A" or guess == "B" or guess =="C" or guess =="D":
            userChoice = True

    if guess == answers[question_num]:
        score += 1
        guesses.append(guess)
        print("CORRECT!")
    else:
        print("INCORRECT!")
        
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1

print("------------------")
print("        RESULTS             ")
print("------------------")

print("answers: ", end="")

for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100 )
print(f"Your score is: {score}%")