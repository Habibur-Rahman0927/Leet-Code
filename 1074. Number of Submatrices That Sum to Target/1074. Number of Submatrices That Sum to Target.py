import collections
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        sub_sum = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                top = sub_sum[r - 1][c] if r > 0 else 0
                left = sub_sum[r][c - 1] if c > 0 else 0
                top_left = sub_sum[r - 1][c - 1] if min(r, c) > 0 else 0
                sub_sum[r][c] = matrix[r][c] + top + left - top_left

        res = 0
        for r1 in range(ROWS):
            for r2 in range(r1, ROWS):
                count = collections.defaultdict(int)
                count[0] = 1
                for c in range(COLS):
                    cur_sum = sub_sum[r2][c] - (
                        sub_sum[r1 - 1][c] if r1 > 0 else 0
                    )
                    diff = cur_sum - target
                    res += count[diff]
                    count[cur_sum] += 1
        return res 
solution = Solution()
print(solution.numSubmatrixSumTarget(matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0))