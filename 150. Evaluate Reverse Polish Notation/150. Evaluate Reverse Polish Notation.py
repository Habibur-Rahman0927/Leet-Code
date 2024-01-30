class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        number_stack = []
        for token in tokens:
            if len(token) > 1 or token.isdigit():
                number_stack.append(int(token))
            else:
                if token == "+":
                    number_stack[-2] += number_stack[-1]
                elif token == "-":
                    number_stack[-2] -= number_stack[-1]
                elif token == "*":
                    number_stack[-2] *= number_stack[-1]
                else:
                    number_stack[-2] = int(float(number_stack[-2]) / number_stack[-1])
                number_stack.pop()
        return number_stack[0]

solution = Solution()
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))