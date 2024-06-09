from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        res = 0
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1

        for n in nums:
            prefix_sum += n
            remain = prefix_sum % k
            res += prefix_cnt[remain]
            prefix_cnt[remain] += 1
        return res
    

solution = Solution()
print(solution.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))