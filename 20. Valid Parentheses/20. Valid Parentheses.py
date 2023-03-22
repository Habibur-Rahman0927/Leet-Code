class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False
        
        opening = set('([{')
        
        matches = set([('{', '}'), ('(', ')'), ('[', ']')])

        stack = []

        for peran in s:
            if peran in opening:
                stack.append(peran)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                if (last_open, peran) not in matches:
                    return False
                
        return len(stack) == 0





solution = Solution()
print(solution.isValid('()[]{}'))