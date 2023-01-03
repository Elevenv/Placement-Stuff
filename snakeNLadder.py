import random

ladders = {3:22,5:8,11:26,20:29}
snakes = {17:4,19:7,21:9,27:1}

currPosition = 0
attempts = 0

while True:
    
    if currPosition == 30:
        print('YOU WON')
        print('totoal numbers of attempts are : ',attempts)
        break
    
    inp = input("Roll dice (type roll) ")

    dice = random.randint(0,6)
    print('Dice score is : ',dice)
    if not currPosition+dice>30:
        currPosition+=dice

    if currPosition in ladders.keys():
        print("Used ladder ")
        currPosition = ladders[currPosition]
    
    elif currPosition in snakes.keys():
        print("Sollow by snake")
        currPosition = snakes[currPosition]

    print('Your current position is : ',currPosition)
    print('\n')

    attempts+=1
