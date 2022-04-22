# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# it is just fibonacci number!!!!!
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = [0] * (n+1)
        if(n==1):
            return 1
        else:
            step[1] = 1
            step[2] = 2
            for i in range(3,n+1):
                step[i] = step[i-1] + step[i-2]
        return step[n]