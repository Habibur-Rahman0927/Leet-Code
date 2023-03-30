class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_arr = s.split()

        return len(list_arr[len(list_arr) - 1])




solution = Solution()
print(solution.lengthOfLastWord("Hello World"))