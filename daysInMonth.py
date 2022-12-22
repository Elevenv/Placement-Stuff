# https://www.codechef.com/problems/NW1

def DayOfMonth(w,s):
    rem = w%7
    day = {"mon":0,"tues":1,"wed":2,"thurs":3,"fri":4,"sat":5,"sun":6}
    l1 = ["4","4","4","4","4","4","4"]
    # d = {"mon":4,"tues":4,"wed":4,"thurs":4,"fri":4,"sat":4,"sun":4}
    # print(d)
    # i = rem
    startDay = day[s]
    while rem>0:
        l1[startDay] =  str(int(l1[startDay]) +1 )
        if startDay ==6:
            startDay = 0
        else:
            startDay +=1
        rem-=1

    s = " ".join(l1)
    return s

for _ in range(int(input())):
    w,s = map(str,input().split())
    w = int(w)
    print(DayOfMonth(w, s))
