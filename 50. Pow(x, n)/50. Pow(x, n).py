class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
    
solution = Solution()
print(solution.myPow(2.00000, 10))