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
        return helper(n)
def helper(n,memo={}):
    if (n<=1): return 1
    if (n in memo): return memo[n]
    memo[n] = helper(n-1,memo) + helper(n-2,memo)
    return memo[n]