class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n < 0 else bin(n).count('1') == 1
solution = Solution()
solution.isPowerOfTwo(16)