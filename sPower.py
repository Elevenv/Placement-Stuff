n = int(input())
names = []
for i in range(n):
    names.append(input())
for name in names:
    sum = 0
    name1 = ''.join(sorted(name))
    j = 1
    for char in name1:
        sum+=(ord(char)-96)*j
        j+=1
    print(sum)






