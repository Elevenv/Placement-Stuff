#given two array pant_prize and shirt_prize
#print best shirt and pant prize below budget

shirt_prize = [10,45,65,23,64,20]
pant_prize = [84,33,56,78,66,20]
budget = int(input())
below_budget = []
for i in range(0,len(pant_prize)):
    if shirt_prize[i] + pant_prize[i]<=budget:
        below_budget.append([shirt_prize[i],pant_prize[i]])
below_budget.sort()
print(below_budget[len(below_budget)-1])