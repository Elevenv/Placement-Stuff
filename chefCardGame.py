# https://www.codechef.com/submit/CRDGAME
# Chef and card game

def Sum(n):
    sum = 0
    while n!= 0:
        sum = sum + (n % 10)
        n = n//10
    return sum

for _ in range(int(input())):
    rounds = int(input())
    chefPoints = 0
    montyPoints = 0
    for i in range(rounds):
        a,b = map(int,input().split())
        a = Sum(a)
        b = Sum(b)
        if a>b:
            chefPoints+=1
        elif b>a:
            montyPoints+=1
        else:
            montyPoints+=1
            chefPoints+=1
    if chefPoints>montyPoints:
        print(0,chefPoints)
    elif montyPoints>chefPoints:
        print(1,montyPoints)
    else:
        print(2,chefPoints)