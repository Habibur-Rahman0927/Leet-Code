class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # stringToArray = s.split(' ')
        # result = []
        # for i in range(len(stringToArray) - 1 , -1, -1):
        #     if stringToArray[i]:
        #         result.append(stringToArray[i])
        #     print(stringToArray[i])
        
        # return ' '.join(result)

        words = s.split()
        
        reversed_words = words[::-1]
        
        reversed_string = ' '.join(reversed_words)
        
        return reversed_string

        # return " ".join(s.strip().split()[::-1])


solution = Solution()
print(solution.reverseWords("the sky is blue"))