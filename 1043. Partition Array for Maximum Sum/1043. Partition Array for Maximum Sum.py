class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        dp = [0] * k
        dp[0] = arr[0]

        for i in range(1, len(arr)):
            cur_max = 0
            max_at_i = 0
            for j in range(i, i - k, -1):
                if j < 0:
                    break
                cur_max = max(cur_max, arr[j])
                window_size = i - j + 1
                cur_sum = cur_max * window_size
                sub_sum = dp[(j - 1) % k] if j > 0 else dp[-1]
                max_at_i = max(max_at_i, cur_sum + sub_sum)
            dp[i % k] = max_at_i
        return dp[(len(arr) - 1) % k]

solution = Solution()
print(solution.maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3))