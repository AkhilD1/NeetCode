# Best Time to Buy and Sell Stock
# Solved 
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:

# Input: prices = [10,8,7,5,2]

# Output: 0

def stock_buy_sell(prices):
    res = 0
    min_price = prices[0]
    for i in prices[1:]:
        if i < min_price:
            min_price = i
        res = max(res, i- min_price)
    return res
print(stock_buy_sell(prices = [10,8,7,5,2]))