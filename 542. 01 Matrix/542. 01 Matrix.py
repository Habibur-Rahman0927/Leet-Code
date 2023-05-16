import collections
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        q = collections.deque()
        row = len(mat)
        col = len(mat[0])
        dirs = [(-1,0), (0,-1), (1,0), (0, 1)] 

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = float("inf")
        
        while q:
            i, j = q.popleft()
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < row and 0 <= y < col and mat[x][y] > mat[i][j] + 1:
                    q.append((x,y))
                    mat[x][y] = mat[i][j] + 1
        return mat
solution = Solution()
print(solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))