class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited=set()
        max_size = 0
        row,col = len(grid),len(grid[0])
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        def dfs(x, y):
            area = 1
            for dx, dy in directions:
                nx,ny = x+dx, y+dy
                if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited and grid[nx][ny]:
                    visited.add((nx,ny))
                    area+=dfs(nx,ny)
            return area
        
        for x in range(row):
            for y in range(col):
                if grid[x][y] and (x,y) not in visited:
                    visited.add((x,y))
                    max_size = max(dfs(x,y), max_size)
        return max_size
    

solution = Solution()
print(solution.maxAreaOfIsland([0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]))