rng = int(input())
s1 = set(map(int,input().split()))
n = int(input())
for i in range(0,n):
    l2 = input().split()
    if l2[0]=='remove':
        s1.remove(int(l2[1]))
    elif l2[0]=='discard':
        s1.discard(int(l2[1]))
    else:
        s1.pop()
print(sum(s1))