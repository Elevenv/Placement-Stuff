# https://www.codechef.com/problems/DWNLD

# cook your dish here
for _ in range(int(input())):
    n,k = map(int,input().split())
    charges = 0
    for i in range(n):
        t,d = map(int,input().split())
        # rem = k-t
        if k>0:
            k-=t
            # if k>0:
            #     continue
            if k>=0:
                continue
            charges = charges + (abs(k)*d)
            # k-=t
        else:
                charges = charges + (t*d)
    
    print(charges)