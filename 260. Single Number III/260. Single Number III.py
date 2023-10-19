class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        return [key for key, value in count.items() if value == 1]