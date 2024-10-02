print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")

if playing.lower() == "yes" :
   print("Rules for the quiz: \n 1)For each correct answer you willscore 4 point. \n 2) For each incorrect question -1 will be deducted. ")
   score=0
   
else :
     quit()



answer =input("In which year India won it's first worldcup. ")
if answer.title()=="1983":
    print("Correct")
    score +=4
else:
    print("Incorrect")
    score -=1

answer=input(str("Who is god of cricket. "))

if answer == "sachin" :
    print("Correct")
    score +=4
else:
    print("Incorrect")
    score -=1    

answer=input("How  many ODI worldcups India has won till date. ")
if answer.title()=="2":
    print("Correct")
    score +=4
else:
    print("Incorrect")
    score -=1
print("you got "+ str(score) +"marks.")   

   


   


