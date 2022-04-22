class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if(numRows == 1):
            outer = [[1]]
        elif numRows == 1: return [[1]]

        outer = [[1]]
        for i in range(1,numRows):
            inner = [1]
            for j in range(1, i):
                inner.append(outer[i-1][j-1]+outer[i-1][j])
            inner.append(1)
            outer.append(inner)
        return outer