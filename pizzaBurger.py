# https://www.codechef.com/submit/PIZZA_BURGER
# Pizza Burger

for _ in range(int(input())):
    x,y,z = map(int,input().split())

    if x>y and x>z:
        print('Pizza')
    elif x>y:
        print('Pizza')
    elif x>z:
        print('Burger')
    else:
        print('Nothing')