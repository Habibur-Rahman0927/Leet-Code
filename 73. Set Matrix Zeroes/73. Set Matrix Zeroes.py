class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_flag = 0 in matrix[0]
        col_flag = 0 in list(zip(*matrix))[0]
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if row_flag:
            matrix[0] = [0] * cols

        if col_flag:
            for row in matrix:
                row[0] = 0
        return matrix
solution = Solution()
print(solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))