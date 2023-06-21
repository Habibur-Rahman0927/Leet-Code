class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        cas_prev = self.countAndSay(n - 1)
        i = 0
        say = ''
        while i < len(cas_prev):
            digit = cas_prev[i]
            count = 0
            while i < len(cas_prev) and cas_prev[i] == digit:
                count += 1
                i += 1
            say += str(count)
            say += str(digit)
        return say
    
solution = Solution()
print(solution.countAndSay(4))