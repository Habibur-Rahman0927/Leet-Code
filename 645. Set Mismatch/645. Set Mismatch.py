import collections
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0, 0]
        count = collections.Counter(nums)

        for i in range(1, len(nums) + 1):
            if count[i] == 0:
                res[1] = i
            if count[i] == 2:
                res[0] = i
        return res

solution = Solution()
print(solution.findErrorNums([1,2,2,4]))