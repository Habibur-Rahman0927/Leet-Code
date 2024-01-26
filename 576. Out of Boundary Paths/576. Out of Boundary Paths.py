class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        
        dp = [[[None] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        self.m = m
        self.n = n
        self.mod = 10**9 + 7
        return self.helper(maxMove, startRow, startColumn, dp)

    def helper(self, maxMove, x, y, dp):
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return 1
        if maxMove <= 0:
            return 0
        if dp[x][y][maxMove] is not None:
            return dp[x][y][maxMove]
        res = 0

        res = (res + self.helper(maxMove - 1, x + 1, y, dp)) % self.mod
        res = (res + self.helper(maxMove - 1, x, y - 1, dp)) % self.mod
        res = (res + self.helper(maxMove - 1, x - 1, y, dp)) % self.mod
        res = (res + self.helper(maxMove - 1, x, y + 1, dp)) % self.mod

        dp[x][y][maxMove] = res

        return res