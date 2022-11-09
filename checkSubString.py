#Check Given string is substring of Main string.

s = 'ThisIsString'
SearchStr = 'ring'

i = 0
flag = False
while i<len(s):
    ct = 0
    if s[i]==SearchStr[0]:
        idx = 0
        for j in range(i,i+len(SearchStr)):
            if s[j]==SearchStr[idx]:
                ct+=1
                idx+=1

    if ct==len(SearchStr):
            flag = True
            break
    i+=1

print(f'{SearchStr} is Substring of {s}') if flag else print(f'{SearchStr} is not Substring of {s}')