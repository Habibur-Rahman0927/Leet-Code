class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        res = []

        for word in words:
            res.append(word[::-1])
        return " ".join(res)