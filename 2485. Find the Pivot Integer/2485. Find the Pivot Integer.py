class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        numbers = []
        for i in range(1, n + 1):
            numbers.append(i)
        
        for pivot in range(n):
            after = sum(numbers[:pivot + 1])
            before = sum(numbers[pivot:])
            if after == before:
                return pivot + 1
        return -1 


solution = Solution()
print(solution.pivotInteger(8))