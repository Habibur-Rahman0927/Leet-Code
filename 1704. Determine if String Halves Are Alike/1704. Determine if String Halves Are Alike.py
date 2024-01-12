class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def getVowel(s):
            return sum(x in 'aeiou' for x in s.lower())

        n = len(s)
        return getVowel(s[:n//2]) == getVowel(s[n//2:])


