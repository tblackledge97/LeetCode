class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # minimum 3
        # only digits and letters
        # at least 1 vowel
        # at least 1 consonant

        if len(word) < 3:
            return False

        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel_seen = False
        cons_seen = False

        for i in range(len(word)):
            # if word is a special character return false
            if not word[i].isalnum():
                return False
            # if letter is a vowel change seen vowel to be True
            elif word[i] in vowel:
                vowel_seen = True
            # if letter is a cons change seen cons to be True
            elif word[i].isalpha() and word[i] not in vowel:
                cons_seen = True
            

        if vowel_seen and cons_seen:
            return True
        else:
            return False