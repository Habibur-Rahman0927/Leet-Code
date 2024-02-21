class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        i = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            i += 1
        return left << i

solution = Solution()
print(solution.rangeBitwiseAnd(5,7))