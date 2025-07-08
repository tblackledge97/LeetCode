class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # convert num1 to int
        num1 = int(num1)
        # convert num2 to int
        num2 = int(num2)

        output = num1 * num2
        output = str(output)
        return output