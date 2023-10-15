class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        N, M = len(matrix), len(matrix[0])
        r, c = N - 1, 0

        while r >= 0 and c < M:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                c += 1
            else:
                r -= 1
        return False

solution = Solution()
print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
