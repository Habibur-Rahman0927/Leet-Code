class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if row == 0 and col != 0:
                    grid[row][col] += grid[row][col - 1]
                elif col == 0 and row != 0:
                    grid[row][col] += grid[row - 1][col]
                elif row != 0 and col != 0:
                    grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        return grid[row][col]
        
solution = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))