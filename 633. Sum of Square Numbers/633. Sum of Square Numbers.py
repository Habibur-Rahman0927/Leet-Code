from math import sqrt
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left, right = 0, int(sqrt(c))
        while left <= right:
            total = left * left + right * right
            if total > c:
                right -= 1
            elif total < c:
                left += 1
            else:
                return True
        return False
solution = Solution()
solution.judgeSquareSum(5)