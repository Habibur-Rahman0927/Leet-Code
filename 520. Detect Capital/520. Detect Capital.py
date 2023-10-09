class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word:
            return True
        elif word.lower() == word:
            return True
        elif word[0].upper() == word[0] and word[1:].lower() == word[1:]:
            return True
        else:
            return False