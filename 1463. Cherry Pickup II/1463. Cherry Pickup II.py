class Solution(object):
    def cherryPickup(self, grid):

        rows, cols = len(grid), len(grid[0])
        memo = {}
        
        def dp(r, c1, c2):
            if r == rows or c1 < 0 or c1 == cols or c2 < 0 or c2 == cols:
                return 0
            if (r, c1, c2) in memo:
                return memo[(r, c1, c2)]
            cherries = grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)
            max_cherries = 0
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    max_cherries = max(max_cherries, dp(r + 1, c1 + dc1, c2 + dc2))
            result = cherries + max_cherries
            memo[(r, c1, c2)] = result
            return result
        return dp(0, 0, cols - 1)