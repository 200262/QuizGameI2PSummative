import datetime
todaydate=datetime.date.today()
#importing the date

name = input("What is your name?")
name = name.upper()
#getting name and making it uppercase
print ("Hello", name, ", this is my quiz game. It is very simple. ""With every question there will be four possible answers, A through D. Just type "
                      "the letter of your answer. At the end you’ll get your score, along with the correct answers. Press enter to begin. Good luck!")
#opening sequence
file = open('questions.txt', "r+")
#opening a file that contains each question on a separate line
secondfile = open("Answers.txt", "r+")
#opening a file that contains each answer on a separate line

score = 0
#setting a variable for the score
questionnumber = 0
#setting a variable for question number (NOTE: THIS IS IRRELEVANT WITHIN THE C
questionsasked = 0
#setting a variable for how many questions have been asked



def askquestion():
    global questionsasked
    #creating a global variable to prevent problems later
    while questionsasked >= 0 and questionsasked < 15:
        #running a while loop that will run for the duration of every question
        global score
        #creating a global variable to prevent problems later
        print(file.readline())
        #prints the next line in the text file "file", which corresponds to the questions text file
        answer = input("Press the letter that corresponds to the correct answer:")
        answer=str(answer)
        answer=answer.upper()
        #asks for answer and converts it to uppercase so that it will correspond with the text file which is in uppercase
        correct=secondfile.readline()
        correct=correct[0]
        correct=str(correct)
        #gets a variable for the correct answer by taking the next line in the text file "secondfile" which corresponds to the answers text file
        if correct==answer:
            score=score+1
            print ("You were correct. Your score is: ", str(score))
            questionsasked=questionsasked+1
            askquestion()
            #if user is correct, one point is added to their score, the question is accounted for and the loop is run again for the next line
        else:
            print ("You were incorrect. The correct answer is:", correct)
            print ("Your score is: ", str(score))
            questionsasked=questionsasked+1
            askquestion()
            #if user is incorrect, the question is accounted for and the loop is run again for the next line

askquestion()
#starts running the loop

print (name, ",", str(score), "out of 15 was your score, completed on", todaydate)
#prints a statement recording your score
fourthfile=open("List of Scores", "r+")
fourthfile.writelines(["\n", str(score)])
fourthfile=sorted(fourthfile.readlines())
scoreslist=[]
#opens a file that can be read and written in, adds the user's score to the list of scores and then sorts this list
for line in fourthfile:
    scoreslist.append(line)
highscore=int(scoreslist[-1])
#creates a variable highscore based on the highest score in the text file
if score >= highscore:
    print ("You have gotten the highest score!")
    #if their score is the highest, then it tells them
else:
    print ("The highest score is:", str(highscore), "Keep trying and you may get it.")
    #if their score is not the highest, it tells them what the highest score is
thirdfile=open("List of Entries", "a")
#opens a file that can be appended
resultline=(name, "got", score, "on", todaydate)
#creates a result line that can be saved
resultline=str(resultline)
thirdfile.writelines(resultline)
#adds this result line to the bank of result lines
