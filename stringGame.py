# https://www.codechef.com/NOV221D/problems/ABSTRING

n = 6
# s = "pqprqr"
s ="cbcba"

l = []

for j in s:
    if j not in l:
        l.append(j)
    else:
        l.remove(j)
print(l)  
print("NO") if l else print("YES")