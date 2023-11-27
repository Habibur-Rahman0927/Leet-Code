import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        ans = []
        count = collections.Counter(nums1)

        for num in nums2:
            if count[num] > 0:
                ans.append(num)
                count[num] -= 1

        return ans

solution = Solution()
print(solution.intersect([4,9,5], [9,4,9,8,4]))