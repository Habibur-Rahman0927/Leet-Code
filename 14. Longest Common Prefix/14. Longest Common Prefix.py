class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs) == 0):
            return ''

        prefix = strs[0]

        for s in strs[1:]:
            if(len(prefix) > len(s)):
                prefix = prefix[0:len(s)]
            while((s.find(prefix) != 0) and (prefix != '')):
                prefix = prefix[0:-1]
        return prefix

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))

