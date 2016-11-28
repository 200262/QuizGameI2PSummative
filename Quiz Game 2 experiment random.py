import datetime
todaydate=datetime.date.today()
#importing the date

name = input("What is your name?")
name = name.upper()
#getting name and converting to uppercase
print ("Hello", name, ", this is my quiz game. It is very simple. ""With every question there will be four possible answers, A through D. Just type "
                      "the letter of your answer. At the end you’ll get your score, along with the correct answers. Press enter to begin. Good luck!")
#opening sequence
file = open('questions.txt', "r+")
secondfile = open("Answers.txt", "r+")
#opening questions and answers text files
score = 0
#setting a variable for score
questionsasked = 0
#getting a variable to count questions asked

from random import shuffle
x=[i for i in range(15)]
#setting a variable that picks from one to fifteen
shuffle(x)
#shuffles x so that each number comes up once and only once
counter=0
RandomVariable=x[counter]
#sets up a variable so that the program can control when x moves on to the next term

questions=[line.rstrip('\n') for line in file]
answers=[line.rstrip('\n') for line in secondfile]
#makes sure that the line from questions will correspond with the line from answers

def askquestion(RandomVariable):
    global questionsasked
    global questions
    global answers
    global counter
    global score
    #sets a few variables global to prevent trouble later
    print(questions[RandomVariable])
    #prints a random question
    answer = input("Press the letter that corresponds to the correct answer:")
    answer=str(answer)
    answer=answer.upper()
    #gets answer and changes it to uppercase so it will correspond with correct answers
    correct=answers[RandomVariable]
    correct=correct[0]
    correct=str(correct)
    #gets correct answer and makes it a string
    if correct==answer:
        score=score+1
        print ("You were correct. Your score is: ", str(score))
        questionsasked=questionsasked+1
        #if answer is correct, score is added and one question is accounted for
        while questionsasked < 15:
            counter=counter+1
            RandomVariable=x[counter]
            askquestion(RandomVariable)
            #if we have not asked all 15 questions, then it will run the function on the next term in x
    else:
        print ("You were incorrect. The correct answer is:", correct)
        print ("Your score is: ", str(score))
        questionsasked=questionsasked+1
        #if the answer is incorrect, one question is accounted for
        while questionsasked<15:
            counter=counter+1
            RandomVariable=x[counter]
            askquestion(RandomVariable)
            #if we have not asked all 15 questions, then it will run the function on the next term in x

askquestion(RandomVariable)
#runs the function at the very beginning, because of the while loop within the function, it ends by itself

print (name, ",", str(score), "out of 15 was your score, completed on", todaydate)
#final score statement
fourthfile=open("List of Scores", "r+")
#opens a file for the list of scores that can be read and written
fourthfile.writelines(["\n", str(score)])
#adds the user's score to this file
fourthfile=sorted(fourthfile.readlines())
#reads this file and then sorts it
scoreslist=[]
#creates a list called scoreslist
for line in fourthfile:
    scoreslist.append(line)
#adds every score into scoreslist
highscore=int(scoreslist[-1])
#makes the highscore the integer value of the highest term in scoreslist (which would the last term)
if score > highscore:
    print ("You have gotten the highest score!")
    #if the user got the high score, they are notified
else:
    print ("The highest score is:", str(highscore), "Keep trying and you may get it.")
    #if the user did not get the high score, they are notified
thirdfile=open("List of Entries", "a")
#opens a file for listing entries, that can be added to
resultline=(name, "got", score, "on", todaydate)
resultline=str(resultline)
#creates a result line that will be added to the list of entries
thirdfile.writelines(resultline)
#adds the result line to the list of entries 
