class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 1
        if s == '':
            return 0
        for i in range(len(s)):
            substring = s[i]
            for j in range(i+1, len(s)): 
                if s[j] not in substring:
                    substring = substring + s[j]
                    maxLen = max(maxLen, len(substring))
                else:
                    break
        return maxLen
    
solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))