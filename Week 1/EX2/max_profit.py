prices = list(map(int, input('Prices:').split()))
def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit
print(max_profit(prices)) 