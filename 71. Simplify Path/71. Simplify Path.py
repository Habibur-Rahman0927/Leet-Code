class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        cur = ""

        for c in path + '/':
            if c == '/':
                if cur == '..':
                    if stack: stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                 cur += c
        return "/" + "/".join(stack)
    
solution = Solution()
print(solution.simplifyPath("/home//foo/"))