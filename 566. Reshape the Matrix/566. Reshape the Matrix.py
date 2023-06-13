class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row, col  = len(mat), len(mat[0])
        if row * col != r * c:return mat
        long_list, result = [], []
        for row in mat:
            for col in row:
                long_list.append(col)
        for i in range(0, len(long_list), c):
            result.append(long_list[i:i+c])
        return result

mat = [[1,2],[3,4]]
r = 1
c = 4
solution = Solution()
print(solution.matrixReshape(mat, r, c))