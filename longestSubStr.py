class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        start = 0
        max_substr_len = 0

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            
            char_index[char] = i
            max_substr_len = max(max_substr_len, i - start + 1)

        return max_substr_len
            