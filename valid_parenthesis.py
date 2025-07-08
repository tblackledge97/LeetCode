class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack of characters
        # push openning characters to top of stack
        # when next character is closing, check is top
        # of stack is the openning equivelant, if it is
        # pop it
        # if stack is empty at the end, it is valid
        
        # list of openning characters
        opening_chars = ['(', '{', '[']

        # list of closing characters
        closing_chars = [')', '}', ']']

        # dictionary of characters
        # key is openning, value is closing
        chars = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }

        stack = []

        for i in range(len(s)):
            # if s[i] is an openning bracket (key in chars)
            # push it to top of stack
            if s[i] in chars:
                stack.append(s[i])
            # if the stack is not empty
            # and
            # if s[i] is the top of the stacks key, value
            elif stack and s[i] == chars[stack[-1]]: 
                # pop it
                stack.pop()
                # otherwise it is not valid
            else:
                return False
        
        # if stack isn't empty, its not valid
        if stack:
            return False
        else: 
            return True
