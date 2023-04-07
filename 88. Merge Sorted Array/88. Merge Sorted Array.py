class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        pointer = len(nums1) - 1
        m = m - 1
        n = n - 1
        
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[pointer] = nums1[m]
                m -= 1
            else:
                nums1[pointer] = nums2[n]
                n -= 1
                
            pointer -= 1
            
        if n >= 0:
            nums1[:n+1] = nums2[:n+1]
        return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution = Solution()
print(solution.merge(nums1, m, nums2, n))
