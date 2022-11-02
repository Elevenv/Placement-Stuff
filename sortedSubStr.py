# https://www.codechef.com/submit/SSUBSTR
# Sorted substrings

s = "011010"
ct = 0

for i in range(len(s)-1):
    if s[i]=='1' and s[i+1]=='0':
        ct+=1

print(ct)