# https://www.codechef.com/submit/STRP
# String Protocol


for _ in range(int(input())):
    n = int(input())
    s = input()
    ct = 0
    i = 0
    while i<len(s):
        if i<len(s)-1:
            if s[i]==s[i+1]:
                ct+=1
                i+=2
            else:
                ct+=1
                i+=1
        else:
            ct+=1
            i+=1
    print(ct)