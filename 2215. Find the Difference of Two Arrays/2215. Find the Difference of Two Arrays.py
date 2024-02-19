class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # array1 = []
        # array2 = []
        # for num1 in nums1:
        #     if num1 not in nums2:
        #         if num1 not in array1:
        #             array1.append(num1)

        # for num2 in nums2:
        #     if num2 not in nums1:
        #         if num2 not in array2:
        #             array2.append(num2)
        # return [array1, array2]

        # set1=set(nums1)
        # set2=set(nums2)
        # diff1=set1-set2
        # diff2=set2-set1
        # print(diff1,diff2)
        # return [diff1,diff2]

        set1 = set(nums1)
        set2 = set(nums2)
        for n in nums2:
            if n in set1 and n in set2:
                set1.remove(n)
                set2.remove(n)
        return [list(set1), list(set2)]
solution = Solution()
print(solution.findDifference([1,2,3], [2, 4, 6]))