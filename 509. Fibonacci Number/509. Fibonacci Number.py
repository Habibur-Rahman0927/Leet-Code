class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n

        dp = [0, 0, 1]

        for i in range(2, n + 1):
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = dp[0] + dp[1]

        return dp[2]

solution = Solution()
print(solution.fib(3))