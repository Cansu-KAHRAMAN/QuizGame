#quiz game
def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1  #current ques num

    for key in questions:
        print("-------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input("Enter(A,B,C or D): ")
        guess= guess.upper()
        guesses.append(guess)    

        correct_guesses += check_answer(questions.get(key),guess)  
        question_num +=1  

    display_score(correct_guesses,guesses)

def check_answer(answer,guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")  
        return 0  

def display_score(correct_guesses, guesses):
    print("--------")
    print("results")
    print("--------")
    print("answers: ", end="")

    for i in questions:
        print(questions.get(i), end=" ")
    print()  #\n

    print("guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()  #\n

    score = int(correct_guesses/len(questions)*100)
    print("your score is: "+str(score)+"%")
    
def play_again():
    response=input("do you want to play again? (yes/no): ")
    response= response.upper()  

    if response == "YES":
        return True
    else:
        return False
 
questions={"QUESTION 1":"A", "QUESTION 2":"B", "QUESTION 3":"C", "QUESTION 4":"B"}
options=[["A","B","C","D"], ["A","B","C","D"], ["A","B","C","D"], ["A","B","C","D"]]

new_game()

while play_again():
    new_game()
print("bye")   

# def play_again():
#   pass
