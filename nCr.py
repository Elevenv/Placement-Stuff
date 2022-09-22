def fact(i):
    f = 1
    while i!=0:
        f = f*i
        i-=1
    return f
n = int(input())
r = int(input())
m = int(input())

print(int((fact(n)/(fact(r)*fact(n-r)))%m))

# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)