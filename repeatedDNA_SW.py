class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Store what has been seen
        seen = set()
        # Store what has been repeated
        repeated = set()

        # left and right pointers
        left = 0
        right = 10

        while right <= len(s):
            # the substring to compare
            substr = s[left:right]
            # if the substring has been seen before, it is repeated
            if substr in seen:
                repeated.add(substr)
            # otherwise add it to what has been seen before
            else:
                seen.add(substr)
            
            # right and left pointer move forward
            right += 1
            left += 1

        return list(repeated)


            