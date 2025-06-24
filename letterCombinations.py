def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # create a map of the digits
        dig_to_char = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        # output list
        output = list()
        
        # backtracking function
        def backtrack(index, current_string):
            # one letter per digit, add to output
            if index == len(digits):
                output.append(current_string)
                return
            # loop over each character
            for char in dig_to_char[digits[index]]:
                # recursion 
                # add character to each string
                # move to next character
                backtrack(index + 1, current_string + char)

        backtrack(0, "")
        return output