from collections import Counter
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = Counter(nums)
        
        count = 0
        for t in mp.values():
            if t == 1:
                return -1
            count += t // 3
            if t % 3:
                count += 1
                
        return count

solution = Solution()
print(solution.minOperations([2,3,3,2,2,4,2,3,4]))