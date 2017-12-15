class Solution(object): #rank 30%, 找最低价天，与后面的高价天比差值
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        else:
            minPrice = prices[0]
            output = 0
            for i in range(1,len(prices)):
                if prices[i] < minPrice:
                    minPrice = prices[i]
                elif output < (prices[i] - minPrice):
                    output = prices[i] - minPrice
            return output
