class MinStack(object):
  def __init__(self):
    self.stack = []

  def push(self, x):
    mini = x if not self.stack else min(self.stack[-1][1], x)
    self.stack.append([x, mini])

  def pop(self):
    self.stack.pop()

  def top(self):
    return self.stack[-1][0]

  def getMin(self):
    return self.stack[-1][1]





# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()