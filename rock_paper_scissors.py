import random
print("Welcome to ROCK/PAPER/SCISSORS Game.")
computer_wins=0
user_wins=0
options=["rock","paper","scissor"]
while True:
    user_input=0
    user_input=input("Type ROCK/PAPER/SCISSORS or Q to quit ").lower()
    if user_input=="q":
       break
    if user_input not in options:
       continue

    random_number=random.randint(0,2)
    computer_choice=options[random_number]
    f"computer picked,{computer_choice}."
    if user_input=="rock" and computer_choice=="scissor":
        print("you won!")
        user_wins+=1
        continue
    elif user_input=="scissor" and computer_choice=="paper":
        print("you won!")
        user_wins+=1
        continue
    elif user_input=="paper" and computer_choice=="rock":
        print("you won!")
        user_wins+=1
    else:
        computer_wins+=1
        print('You lost !')
        
print(f"you won {user_wins}, times.")   
print(f"computer won {computer_wins},times")
print(f"Goodbye")    
    

 





       





    
 



    
        
    



