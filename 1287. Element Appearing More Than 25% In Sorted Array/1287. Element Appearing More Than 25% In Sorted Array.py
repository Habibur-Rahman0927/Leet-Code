class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # return max(arr, key=arr.count)
        threshold = len(arr) // 4

        frequency_map = {}

        for num in arr:
            frequency_map[num] = frequency_map.get(num, 0) + 1
            if frequency_map[num] > threshold:
                return num
        

solution = Solution()
print(solution.findSpecialInteger([1,2,2,6,6,6,6,7,10]))