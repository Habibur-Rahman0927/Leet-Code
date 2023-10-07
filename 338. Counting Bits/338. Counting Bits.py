class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i // 2] + (i & 1)
        return dp

solution = Solution()
print(solution.countBits(5))