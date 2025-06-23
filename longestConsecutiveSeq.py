def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # convert list to set 
        cons_elements = set(nums)
        # initialize longest streak
        longest = 0

        for num in cons_elements:
            # only start counting if it's the start of a sequence
            if num - 1 not in cons_elements:
                current = num
                streak = 1

                # count the streak
                while current + 1 in cons_elements:
                    current += 1
                    streak += 1

                # longest streak
                longest = max(longest, streak)

        return longest