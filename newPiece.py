# https://www.codechef.com/problems/NEWPIECE


for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    add1 = a+b
    add2 = c+d
    
    if a==c and b==d:
        print("0")
    else:
        if (add1%2==0 and add2%2==0) or (add1%2!=0 and add2%2!=0):
            print("2")
        else:
            print("1")