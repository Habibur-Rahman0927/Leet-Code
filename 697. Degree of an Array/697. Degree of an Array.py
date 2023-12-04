class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        repeatCounts = {}
        lefts = {}
        rights = {}

        for i, v in enumerate(nums):
            if v in repeatCounts:
                repeatCounts[v] += 1
                rights[v] = i
            else:
                repeatCounts[v] = 1
                lefts[v] = i
                rights[v] = i

        maxRepeats = max(repeatCounts.values())

        keys = [key for key, value in repeatCounts.items() if value == maxRepeats]
        
        return min([rights[key] - lefts[key] for key in keys]) + 1


solution = Solution()
print(solution.findShortestSubArray([1,2,2,3,1,4,2]))
        