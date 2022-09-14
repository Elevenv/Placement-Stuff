transactions = list(map(str,input().split()))

temp = []
accNoBalance = {}

for i in transactions:
    temp = i.split('->')
    if temp[0] not in accNoBalance.keys():
        accNoBalance[temp[0]] = int(temp[1])
    else:
        accNoBalance[temp[0]] = int(accNoBalance[temp[0]]) + int(temp[1])
    temp = []
    
for i in accNoBalance:
    print(i , "has Amount of " ,accNoBalance[i])
