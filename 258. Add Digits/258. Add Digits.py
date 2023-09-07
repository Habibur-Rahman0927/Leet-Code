class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        while num > 0:
            ans += num % 10
            num //= 10

            if ans > 9 and num == 0:
                num = ans
                ans = 0
        return ans

solution = Solution()
print(solution.addDigits(38))