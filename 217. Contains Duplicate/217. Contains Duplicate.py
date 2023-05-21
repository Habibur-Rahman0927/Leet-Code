class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashMap = set()

        for num in nums:
            if num in hashMap:
                return True
            hashMap.add(num)
        return False



solution = Solution()
# print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(solution.containsDuplicate([1,2,3,4]))