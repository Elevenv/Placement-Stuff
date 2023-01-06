s = ["h","e","l","l","o"]

# print(s)
# for i in range(len(s)):
#     temp = s.pop()
#     s.insert(i, temp)
# print(s)

for i in range(len(s)//2):
    s[i],s[-1-i] = s[-1-i],s[i]
print(s)