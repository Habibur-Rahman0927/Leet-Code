class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False

        if num == 0 or num == 1:
            return True

        start, end = 1, num // 2

        while start <= end:
            mid = (start + end) // 2
            mid_squared = mid * mid

            if mid_squared == num:
                return True
            elif mid_squared < num:
                start = mid + 1
            else:
                end = mid - 1

        return False

solution = Solution()
print(solution.isPerfectSquare(15))