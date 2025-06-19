def reverse(self, x: int) -> int:
        # if not a - number
        if x > 0:
            # turn the int to a string
            y = str(x)
            # reverse the string
            y = y[::-1]
            # turn the string back to an int
            y = int(y)
        else:
            # remove the -
            y = abs(x)
            # turn into string
            y = str(y)
            # reverse the string
            y = y[::-1]
            # put the negative sign back
            y = -int(y)

        # check it is a 32 bit int
        if y > 2 ** 31 - 1 or y < -2 ** 31:
            y = 0

        return y