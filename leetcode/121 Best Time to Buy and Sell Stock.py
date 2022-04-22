class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minval = 1000000
        maxdif = 0
        for i in range(len(prices)):
            if(prices[i] < minval):
                minval = prices[i]
            elif(prices[i] > minval and prices[i] - minval > maxdif):
                maxdif = prices[i] - minval
        return maxdif
    
    def solution(self,prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minval = float('inf') # proper way to set the upperbound
        maxdif = 0
        for i in range(len(prices)):
            if(prices[i] < minval):
                minval = prices[i]
            elif(prices[i] - minval > maxdif): # remove the redundant comparator that increase the memory usage
                maxdif = prices[i] - minval
        return maxdif