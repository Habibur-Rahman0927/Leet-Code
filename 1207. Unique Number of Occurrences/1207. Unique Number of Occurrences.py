from collections import defaultdict
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arrMap = defaultdict()
        for i in arr:
            if i in arrMap:
                arrMap[i] += 1
            else:
                arrMap[i] = 1
        return len(arrMap.values()) == len(set(arrMap.values()))

solution = Solution()
solution.uniqueOccurrences([1,2,2,1,1,3])
