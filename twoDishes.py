# cook your dish here
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    fm = min(b,c)
    # if b==c and c==d and b==d:
    #     print("YES") if b>=a else print("NO")
    # else:
    print("YES") if (min(b,c)+min(c-fm,d))>=a else print('NO')
