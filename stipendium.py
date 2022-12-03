# https://www.codechef.com/problems/EGRANDR

def check(n,l):

    if (sum(l)/n)<4.0:
        print("No")
    elif 5 in l:
        for k in l:
            if k<=2:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")

n = int(input())
Marks = list(map(int,input().split()))
check(n, Marks)