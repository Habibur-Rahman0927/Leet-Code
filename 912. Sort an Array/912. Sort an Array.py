# 1st approce

# class Solution(object):
#     def sortArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         if len(nums) == 1:
#             return nums
#         mid = int(len(nums)/2)
#         left = nums[:mid]
#         right = nums[mid:]
#         return self.merge(self.sortArray(left), self.sortArray(right))
    
#     def merge(self, arr1, arr2):
#         combined = []
#         i = 0
#         j = 0
#         while i < len(arr1) and j < len(arr2):
#             if arr1[i] < arr2[j]:
#                 combined.append(arr1[i])
#                 i += 1
#             else:
#                 combined.append(arr2[j])
#                 j += 1
#         while i < len(arr1):
#             combined.append(arr1[i])
#             i += 1
#         while j < len(arr2):
#             combined.append(arr2[j])
#             j += 1
#         return combined

#2nd approce
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k > len(right):
                nums[i] = right[j]
                k += 1
                i += 1

        def mergeSort(arr, l, r):

            if l == r:
                return nums
            m = (l + r)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr
        return mergeSort(nums, 0, len(nums) - 1)

    

solution = Solution()
print(solution.sortArray([5,1,1,2,0,0]))