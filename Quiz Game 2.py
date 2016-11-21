name = input("What is your name?")
name = name.upper()
print ("Hello", name, ", this is my quiz game. It is very simple. ""With every question there will be four possible answers, A through D. Just type "
                      "the letter of your answer. At the end you’ll get your score, along with the correct answers. Press enter to begin. Good luck!")

file = open('questions.txt', "r+")
secondfile = open("Answers.txt", "r+")
score = 0

questionnumber = 0
questionsasked = 0

def askquestion(questionnumber):
    global questionsasked
    while questionsasked >= 0 and questionsasked < 7:
        global score
        print(file.readline())
        answer = input("Press the letter that corresponds to the correct answer:")
        answer=str(answer)
        correct=secondfile.readline()
        correct=correct[0]
        correct=str(correct)
        if correct==answer:
            score=score+1
            print ("You were correct. Your score is: ", str(score))
            questionsasked=questionsasked+1
            askquestion(questionnumber + 1)
        else:
            print ("You were incorrect. The correct answer is:", correct)
            print ("Your score is: ", str(score))
            questionsasked=questionsasked+1
            askquestion(questionnumber + 1)

askquestion(questionnumber)
print ("You have completed the game. You're score was:", score)
