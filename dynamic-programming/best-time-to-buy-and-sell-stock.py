class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        high = 0
        low = float('inf')

        for i in prices:
            if i < low: 
                low = i
            elif (i-low) > high:
                high = i - low
        
        return high


        