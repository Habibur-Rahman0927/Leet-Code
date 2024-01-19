class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        N = len(matrix)
        for r in range(1, N):
            for c in range(N):
                mid = matrix[r - 1][c]
                left = matrix[r - 1][c - 1] if c > 0 else float('inf')
                right = matrix[r - 1][c + 1] if c < N - 1 else float('inf')
                matrix[r][c] = matrix[r][c] + min(mid, left, right)
        return min(matrix[-1]) 

solution = Solution()
print(solution.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))