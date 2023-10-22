class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        nums1 = set(nums1)

        for num in nums2:
            if num in nums1:
                ans.append(num)
                nums1.remove(num)

        return ans

solution = Solution()
print(solution.intersection([4,9,5], [9,4,9,8,4]))