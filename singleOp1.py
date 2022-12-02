# https://www.codechef.com/submit/SINGLEOP1
# Single operation part 1

for _ in range(int(input())):
    n = int(input())
    s = input()
    ct = 0
    
    for i in s:
        if i=='0':
            break
        else:
            ct+=1
    print(ct)