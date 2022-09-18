n = 13
if n%6==0:
    print(n//6)
elif n%8==0:
    print(n//8)
elif n%14==0:
    print((n//14)*2)
else:
    print(-1)