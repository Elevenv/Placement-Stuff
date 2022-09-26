maxSize = 3

def push(item,stack):
    if len(stack)<maxSize:
        stack.append(item)
        print(item,' added')
    else:
        print('Stack full')

def pop(stack):
    if len(stack)!=0:
        ele = stack[len(stack)-1]
        stack.pop()
        print(ele,' removed')
    else:
        print('Stack is empty')

stack = []
push(1,stack)
push(2,stack)
push(3,stack)
pop(stack)
print(stack)

# leftOfMax = prices[0:prices.index(max(prices))+1]
# rightOfmax = prices[prices.index(max(prices)):len(prices)]

# small = 0
# print(leftOfMax)
# for i in leftOfMax:
#     if small<prices[len(prices)-1]:
#         small = i

# # leftProfit = max(leftOfMax)-min(leftOfMax)
# # rightProfit = max(rightOfmax)-min(rightOfmax)

# print(max(prices)-small)
# print(rightProfit)

# minPrice = min(prices)
# newPrice = prices[prices.index(minPrice):len(prices)]
# print(prices)
# print(newPrice)
# print(max(newPrice)-minPrice)

# # prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# # prices = [2,4,1]
# max = 0
# for i in range(len(prices)):
#     for j in range(i+1,len(prices)):
#         if prices[j]-prices[i]>max:
#             max = prices[j]-prices[i]
# print(max)

# num = 101
# k = int(num/10)*11
# print(k)