import random
choices=["rock","paper","scissors"]
while(1):
    print("lets play rock, paper, scissors:")
    choice=input("what do you choose?")
    computer_choice=random.choice(choices)
    print("computer choose:",computer_choice)
    if(choice==computer_choice):
        print("this round is draw!")
    elif(choice=="rock" and computer_choice=="scissors"):
        print("you won this round!")
    elif(choice=="paper" and computer_choice=="rock"):
        print("you won this round!")
    elif(choice=="scissors" and computer_choice=="paper"):
        print("you won this round!")
    else:
        print("you lost this round.")
