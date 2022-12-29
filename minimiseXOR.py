# https://www.codechef.com/DEC221C/problems/XORMAX


def minXOR(a,b):
    z = o = 0
    for i in range(len(a)):
        if a[i] == '0':
            z+=1
        else:
            o+=1
        
        if b[i] == '0':
            z+=1
        else:
            o+=1
    print(z,o)
    temp = min(z,o)
    ans = ''
    for i in range(temp):
        ans+='1'
    
    for j in range(temp,len(a)):
        ans+='0'
    
    return ans

for _ in range(int(input())):
    a = input()
    b = input()
    print(minXOR(a, b))