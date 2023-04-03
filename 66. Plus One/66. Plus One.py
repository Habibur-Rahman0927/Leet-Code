class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i, d in reversed(list(enumerate(digits))):
            if d < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
    

# digits = [1,2,3]
# digits = [4,3,2,1]
# digits = [9]
digits = [9, 9, 9, 9]

solution = Solution()
print(solution.plusOne(digits))