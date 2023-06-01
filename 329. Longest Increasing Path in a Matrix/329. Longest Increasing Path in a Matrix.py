class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        dp = {}

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or 
                c < 0 or c == COLS or
                matrix[r][c] <= prevVal): return 0
            print(matrix[r][c])
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            dp[(r, c)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())
    
solution = Solution()
print(solution.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))