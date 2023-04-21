import random
moves = ['rock','paper','scissors']
computers_move=random.choice(moves)
player_move = str(input())
if player_move== computers_move:
    print('Its a draw, player_move again')
elif player_move == 'scissors' and computers_move =='paper':
    print("you won")
elif player_move == 'paper' and computers_move =='rock':
    print("you won")
elif player_move == 'rock' and computers_move =='scissors':
    print("you won")
elif computers_move == 'scissors' and player_move =='paper':
    print('You lost!the computer played: ',computers_move)
elif computers_move == 'paper' and player_move =='rock':
    print('You lost!the computer played: ',computers_move)
elif computers_move == 'rock' and player_move =='scissors':
    print('You lost!the computer played: ',computers_move)

    

