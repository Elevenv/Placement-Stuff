# https://www.codechef.com/submit/NONADJFLIP
#Non Adjancent Flip

for _ in range(int(input())):
    n=int(input())
    s=input()
    if s.count('0')==n:
        print(0)
    else:
        if s.count("11")>0:
            print(2)
        else:
            print(1)