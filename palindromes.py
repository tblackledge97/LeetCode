class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        x_rev_str = x_str[::-1]
        if x_str == x_rev_str:
            return True
        else:
            return False

