# https://www.codechef.com/submit/ALPHABET
# Studying Alphabets

canRead = input()
n = int(input())
l = []
for i in range(n):
    l.append(input())

for j in l:
    for k in j:
        if k not in canRead:
            print('No')
            break
    else:
        print('Yes')