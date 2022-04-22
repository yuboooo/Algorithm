# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxarr = nums[0]
        temp = nums[0]
        for i in range(1,len(nums)):
            if (temp < 0):
                temp = nums[i]
                maxarr = max(temp,maxarr)
            else:
                temp += nums[i]
                maxarr = max(temp,maxarr)
        return maxarr

    def solution(self,nums):
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray