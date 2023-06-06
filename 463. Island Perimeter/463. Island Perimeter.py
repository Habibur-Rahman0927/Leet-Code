class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:return 0
        visit = set()
        def dfs(r, c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 0:
                return 1
            if (r, c) in visit:
                return 0
            visit.add((r, c))
            perim = dfs(r, c + 1)
            perim += dfs(r + 1, c)
            perim += dfs(r, c - 1)
            perim += dfs(r - 1, c)
            return perim

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    return dfs(r, c)
                
solution = Solution()
print(solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))