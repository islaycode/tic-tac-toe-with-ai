from random import randint
player_wins=0
computer_wins=0
winnig_score=3

while player_wins < winnig_score and computer_wins < winnig_score:
    print(f"Player score:{player_wins} Computer score:{computer_wins}")
    print('rock')
    print('paper')
    print('scissor')

    player=input('Please Choose Your move: ').lower()
    if player == "quit" or player =="q":
        break

    random_num=randint(0,2)
    if(random_num==0):
        computer='rock'
    elif(random_num==1):
        computer='scissor'
    else:
        computer='paper'

    print(f'computer plays: {computer}')

    if player == computer:
        print("DRAW")
    
    elif player == 'rock':
        if computer == 'paper':
            print("Computer Wins")
            computer_wins +=1
        else:
            print("Player wins!")
            player_wins +=1
   
    elif player == 'paper':
        if computer == 'rock':
            print("Player Wins")
            player_wins +=1
        else:
            print("Computer wins!")
            computer_wins +=1
 
    elif player == 'scissor':
        if computer == 'paper':
            print("Player Wins")
            player_wins +=1
        else:
            print("Computer wins!")
            computer_wins +=1
    
    else:
        print('Please provide a valid input')

if player_wins > computer_wins:
    print("Congrats Yow Won the GAME!!")

elif player_wins == computer_wins:
    print("IT'S A TIE")
else: 
    print("OH NO :( THE COMPUTER WON...")

