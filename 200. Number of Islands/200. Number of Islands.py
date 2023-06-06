import collections
""" dfs """
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:return 0
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    islands += 1
        return islands
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        direction = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r, c in direction:
            if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == '1':
                self.dfs(grid, r, c)
                
""" bfs """
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:return 0
        islands = 0
        visit = set()

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = r + dr, c + dc
                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == '1' and (r, c) not in visit:
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands

solution = Solution()
print(solution.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))