import random
l = ["rock", "paper", "scissor"]

#  rock vs paper -> paper Wins 
# rock vs scissor -> rock wins
# paper vs scissor -> scissor wins

while True:
    ccount=0
    ucount=0
    uc = int(input('''
Game Start....
1 Yes
2 No  | Exit
    '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1 Rock
2 Scissor
3 Paper                               

'''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"

            Cchoice = random.choice(l)
            if Cchoice == uchoice:
                print("Computer choice ", Cchoice)
                print("User choice ", uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper") :
                print("Computer choice ", Cchoice)
                print("User choice ", uchoice)
                print("You win")
                ucount=ucount+1
               
            else :
                print("Computer choice ", Cchoice)
                print("User choice ", uchoice)
                print("Computer win")
               
                ccount=ccount+1
        print("Final Result")
        if ucount==ccount:
            print("Game Draw")
            print("User Score ", ucount)
            print("Computer Score", ccount)
        elif ucount > ccount :
            print("You win the Game")
            print("User Score ",ucount)
            print("Compuiter Score ",ccount)
        else:
            print("Computer win the Game")
            print("User Score ",ucount)
            print("Computer Score ",ccount)

    else:
        break;    


