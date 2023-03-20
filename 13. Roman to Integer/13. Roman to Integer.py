class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {
            'I':1,
            'V':5,
            'X':10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        N = len(s)
        i = N - 1
        output = 0
        while i >= 0:
            if i < N - 1 and lookup[s[i]] < lookup[s[i+1]]:
                output -= lookup[s[i]]
            else:
                output += lookup[s[i]]
            i -= 1
        return output
    
solution = Solution()

print(solution.romanToInt("MCMXCIV"))

class Solution2(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {
            'I':1,
            'V':5,
            'X':10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        output = 0
        for i in range(len(s)):
            if i + 1 < len(s) and lookup[s[i]] < lookup[s[i + 1]]:
                output -= lookup[s[i]]
            else:
                output += lookup[s[i]]
        return output
    
solution2 = Solution2()

print(solution2.romanToInt("MCMXCIV"))