class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 2]
        if 2 < n:
            for i in range(3, n + 1):
                dp.append(dp[i - 2] + dp[i - 1])
        return dp[n]
    
solution = Solution()
print(solution.climbStairs(3))