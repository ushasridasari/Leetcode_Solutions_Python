class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else :
                l = r
            r += 1
        return maxp

        '''
        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit
        '''
                
        