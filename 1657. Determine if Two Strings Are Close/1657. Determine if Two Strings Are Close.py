class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        return sorted(collections.Counter(word1).values()) == sorted(collections.Counter(word2).values()) and set(word1) == set(word2)