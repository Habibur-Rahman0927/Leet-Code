class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
    
solution = Solution()
print(solution.hammingWeight(11111111111111111111111111111101))