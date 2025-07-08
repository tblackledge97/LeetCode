class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # get rid of all trailing whitespace
        # for every non space, add that character to current_word 
        # every time a space is encountered, clear current_word
        s = s.strip()
        current_word = ""
        for char in s:
            if char != " ":
                current_word = current_word + char
            elif char == " ":
                current_word = ""
            
        return len(current_word)