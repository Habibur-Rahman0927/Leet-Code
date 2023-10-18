class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in {6, 28, 496, 8128, 33550336}
