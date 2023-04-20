import random
x = random.randrange(1,1000)
y = x
y = str(y)
print("Find the value of X!!")
your_score = 100
if int(input()) == x:
    print(f'your score is {your_score}') 
else:
    print("You have two more attempts")
    your_score -= 20
    if len(str(y))> 2:
        print(f"Your first clue is your starting number {y[0]}")
        if int(input()) == x:
            print(f'your score is {your_score}') 
        else:
            print(f"You have one more attempt and your final clue is {y[-1]}")
            your_score -= 20
    
            if int(input()) == x:
                print(f'your score is {your_score}') 
            else:
                print("You have failed!")
                print(f'The correct answer was {x}')
    elif len(str(y))<=2:
        print(f"Your first clue is  its a two digit number and your starting number {y[0]}")
        if int(input()) == x:
            print(f'your score is {your_score}') 
        else:
            print(f"You have failed")