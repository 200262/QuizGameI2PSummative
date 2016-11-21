name = input("What is your name?")
name = name.upper()
print ("Hello", name, ", this is my quiz game. It is very simple. ""With every question there will be four possible answers, A through D. Just type "
                      "the letter of your answer. At the end you’ll get your score, along with the correct answers. Press enter to begin. Good luck!")

questionnumber = 0


questions = ["Question One: What is the seventh planet from the sun? A. Pluto B. Jupiter C. There are only six planets D. Uranus",
             "Question Two: Where would you find the Sea of Tranquility? A. The Moon B. California C. Brazil D. Spain",
             "Question Three: Which chess piece can move diagonally? A. King B. Princess C. Pawn D. Bishop",
             "Question Four: What hormone controls the supply of sugar between muscles and blood? A. Testosterone B. It's controlled by an enzyme, not a hormone C. Insulin D. Glucagon",
             "Question Five: How many symphonies did Beethoven compose? A. 12 B. 9 C. 0 D. 39",
             "Question Six: Which of the following is not a major blood group? A. A B. B C. P D. O ",
             "Question Seven: What is Earth's diameter? A. 8000 miles B. 800 miles C. 10000 kilometers D. It has not been measured yet",
             "Question Eight: How old is Donald Trump? A. 62 B. 10 C. 70 D. 65",
             "Question Nine: How much dirt is there in a hole 4 ft deep by 3 ft wide by 6 ft long? A. 0 cubic ft B. 360 cubic ft C. 100 cubic ft, D. 24 cubic yards",
             "Question Ten: How many US states border the Gulf of Mexico? A. 7 B. 0 C. 1 D. 5",
             "Question Eleven: What colour is Absynth? A. Yellow B. Green C. Orange D. Absynth is not a color",
             "Question Twelve: How many patents did Thomas Edison average per week of his life? A. 17 B. 1/3 C. less than 1/4 D. 2",
             "Question Thirteen: How many times can you subtract 10 from 100? A. Once B. Twice C. 10 times D. an infinite amount of times",
             "Question Fourteen: How many plays did Shakespeare write? A. 37 B. 12 C. He didn't write them D. 56",
             "Question Fifteen: A rooster laid an egg on top of a barn roof, which way did it roll? A. left B. right C. it broke D. none of the above",
             ]
answers = ["D", "A", "D", "C", "B", "C", "A", "C", "A", "D", "B", "B", "A", "A", "D", ]
totalquestions=len(questions)
answerinput=0
score = 0
questionsasked=0
print (totalquestions)

def question(questionnumber):
    global answerinput
    global questionsasked
    while questionsasked >= 0 and questionsasked < totalquestions:
        print (questions[questionnumber])
        answerinput = input("Which answer?")
        answerinput=answerinput.upper()
        answer(questionnumber)

def answer(questionnumber):
    global questionsasked
    while questionsasked >= 0 and questionsasked < totalquestions:
        global score
        global answerinput
        if str(answerinput) == str(answers[questionnumber]):
            score=score+1
            print ("You were correct. You're score is:", str(score))
            questionsasked=questionsasked+1
            question(questionnumber+1)
        else:
            print ("You were incorrect, the correct answer was:", str(answers[questionnumber]))
            print ("You're score is:", str(score))
            questionsasked=questionsasked+1
            question(questionnumber+1)

question(questionnumber)
print ("You have completed the game. You're score was:", score)

