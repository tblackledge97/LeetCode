class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        # longest repeated string
        longest = ""
        
        # look at windows from position 1 to len(s) - 1
        # i acts like a left points
        for i in range(1, len(s)):
            # What we have seen already
            seen = set()
            # J acts like a right pointer
            for j in range(len(s) - i + 1):
                substr = s[j:j + i]
                if substr in seen:
                    if len(substr) > len(longest):
                        longest = substr
                else:
                    seen.add(substr)

        return longest