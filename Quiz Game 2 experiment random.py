import datetime
todaydate=datetime.date.today()


name = input("What is your name?")
name = name.upper()
print ("Hello", name, ", this is my quiz game. It is very simple. ""With every question there will be four possible answers, A through D. Just type "
                      "the letter of your answer. At the end you’ll get your score, along with the correct answers. Press enter to begin. Good luck!")

file = open('questions.txt', "r+")
secondfile = open("Answers.txt", "r+")
score = 0

questionnumber = 0
questionsasked = 0

from random import shuffle
x=[i for i in range(15)]
shuffle(x)
counter=0
RandomVariable=x[counter]
print (x)

questions=[line.rstrip('\n') for line in file]
answers=[line.rstrip('\n') for line in file]

def askquestion(RandomVariable):
    global questionsasked
    global questions
    global answers
    global counter
    while questionsasked >= 0 and questionsasked < 14:
        global score
        print(questions[RandomVariable])
        answer = input("Press the letter that corresponds to the correct answer:")
        answer=str(answer)
        answer=answer.upper()
        correct=answers[RandomVariable]
        correct=correct[0]
        correct=str(correct)
        if correct==answer:
            score=score+1
            print ("You were correct. Your score is: ", str(score))
            questionsasked=questionsasked+1
            counter=counter+1
            RandomVariable=x[counter]
            askquestion(RandomVariable)
        else:
            print ("You were incorrect. The correct answer is:", correct)
            print ("Your score is: ", str(score))
            questionsasked=questionsasked+1
            counter=counter+1
            RandomVariable=x[counter]
            askquestion(RandomVariable)

askquestion(RandomVariable)

print (name, ",", str(score), "out of 15 was your score, completed on", todaydate)
fourthfile=open("List of Scores", "r+")
fourthfile.writelines(["\n", str(score)])
fourthfile=sorted(fourthfile.readlines())
scoreslist=[]
for line in fourthfile:
    scoreslist.append(line)
highscore=int(scoreslist[-1])
if score > highscore:
    print ("You have gotten the highest score!")
else:
    print ("The highest score is:", str(highscore), "Keep trying and you may get it.")
thirdfile=open("List of Entries", "a")
resultline=(name, "got", score, "on", todaydate)
resultline=str(resultline)
print (resultline)
thirdfile.writelines(resultline)
