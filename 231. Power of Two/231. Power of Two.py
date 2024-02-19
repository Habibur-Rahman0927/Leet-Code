class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # return False if n < 0 else bin(n).count('1') == 1
        # if n <= 0: return False
        # if n == 1: return True
        # while n % 2 == 0:
        #     n = n // 2
        # return n == 1


        # aux = 0
        # result = 0

        # while(True):
        #     result = 2**aux
        #     if(result == n):
        #         return True
        #     elif result>n:
        #         return False
        #     aux +=1

        # if n <= 0:
        #     return False
        # while(n != 1):
        #     rem = n%2
        #     if rem > 0:
        #         return False
        #     n = n/2
        # return True

        if n<=0:
            return False
        new_n = n - 1
        return n  & new_n ==0
solution = Solution()
print(solution.isPowerOfTwo(512))