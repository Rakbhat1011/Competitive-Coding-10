"""
Buy before every price increase and sell at the peak — capture every profit
Iterate through prices and add up all increases (prices[i] > prices[i-1])
We can perform multiple buys/sells, so add all positive differences
"""
"""
Time Complexity : O(n) - One pass through all prices
Space Complexity : O(1) - No aixillary
"""

class bestToSell2:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

if __name__ == "__main__":
    obj = bestToSell2()

    prices1 = [7, 1, 5, 3, 6, 4]
    print(obj.maxProfit(prices1))

