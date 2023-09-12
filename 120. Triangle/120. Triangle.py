class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])

        return dp[0]

solution = Solution()
print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))