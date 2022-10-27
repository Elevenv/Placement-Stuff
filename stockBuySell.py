# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# 121. Best Time to Buy and Sell Stock

prices = [7,1,5,3,6,4]

maxProfit = 0
minPurchase = prices[0]
for i in range(len(prices)):
    maxProfit = max(maxProfit,prices[i] - minPurchase)
    minPurchase = min(minPurchase,prices[i])
print(maxProfit)