from collections import defaultdict
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr2_set = set(arr2)
        arr1_count = defaultdict(int)
        end = []
        for n in arr1:
            if n not in arr2_set:
                end.append(n)
            arr1_count[n] += 1
        end.sort()
        res = []

        for n in arr2:
            for _ in range(arr1_count[n]):
                res.append(n)
        return res + end


solution = Solution()
print(solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))