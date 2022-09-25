T = int(input())
for i in range(0,T):
    sum = 0
    a,b=0,0
    no_of_st = int(input())
    time1 = input().split()
    for j in range(len(time1)):
        time = int(time1[j])
        a+=time
        b+=time
        extra_time = a-b+time
        if extra_time>0:
            b+=extra_time
    print(b)