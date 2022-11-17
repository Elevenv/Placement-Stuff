#Check given string is substring or not while considering the sequence 

# a1 = [1, 2, 3, 4]
# a2 = [1, 3, 4]

a1 = [5, 1, 22, 25, 6, 10]
a2 = [1,6,10]

l1 = []
l2 = []

for i in a2:
    l2.append(a1.index(i))

for j in a1:
    if j in a2:
        l1.append(a1.index(j))

if len(l1) == len(l2):
    print(True) if l2 == sorted(l2) else print(False)

