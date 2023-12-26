class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        # l1, l2 = len(str1), len(str2)
        
        # def divisor(l):
        #     if l1 % l or l2 % l:
        #         return False
        #     f1, f2 = l1 // l, l2 // l
        #     return str1[:l] * f1 == str1 and str2[:l] * f2 == str2
        # for l in range(min(len(str1), len(str2)), 0, -1):
        #     if divisor(l):
        #         return str1[:l]
        # return ''

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 == str2 + str1:
            x = gcd(len(str1), len(str2))
            return str1[:x]
        else:
            return ""

solution = Solution()
solution.gcdOfStrings("ABABAB", "ABAB")