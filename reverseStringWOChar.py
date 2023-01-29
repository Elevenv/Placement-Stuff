# s = 'a1b2igh3'  #h1g2iba3
s = 'ab5c7de96'     #ed5c7ba96

ans = ''
l = len(s)-1

for i in s:
    if i.isalpha():
        l-=1
        while l>-1:
            if s[l].isalpha():
                break
            l-=1
        ans = ans+s[l]
    else:
        ans+=i

print(ans)
