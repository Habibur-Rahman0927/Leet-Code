class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sortedNums = sorted(score, reverse=True)
        numsMap = {}
        for i in range(len(sortedNums)):
            if i == 0:
                numsMap[sortedNums[i]] = 'Gold Medal'
            elif i == 1:
                numsMap[sortedNums[i]] = 'Silver Medal'
            elif i == 2:
                numsMap[sortedNums[i]] = 'Bronze Medal'
            else:
                numsMap[sortedNums[i]] = str(i+1)
        result = []
        for num in score:
            result.append(numsMap[num])
        return result
    
solution = Solution()
print(solution.findRelativeRanks([10,3,8,9,4]))