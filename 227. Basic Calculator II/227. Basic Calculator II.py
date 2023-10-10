class Solution:
  def calculate(self, s: str) -> int:
        num_stack = []
        num = 0
        op = '+'
        for s_s in s:
            if s_s == ' ':
                continue
            elif s_s.isdigit():
                num = num * 10 + int(s_s)
            else:
                if op == '*':
                    x = num_stack.pop()
                    num_stack.append(x * num)
                elif op == '/':
                    x = num_stack.pop()
                    if x < 0:
                        num_stack.append(-((-x) / num))
                    else:
                        num_stack.append(x / num)
                elif op == '-':
                    num_stack.append(-1 * num)
                else:
                    num_stack.append(num)
                op = s_s
                num = 0
        else:
            if op == '*':
                x = num_stack.pop()
                num_stack.append(x * num)
            elif op == '/':
                x = num_stack.pop()
                if x < 0:
                    num_stack.append(-((-x)/ num))
                else:
                    num_stack.append(x / num)
            elif op == '-':
                num_stack.append(-1 * num)
            else:
                num_stack.append(num)
        return sum(num_stack)

solution = Solution()
print(solution.calculate("3+2*2"))