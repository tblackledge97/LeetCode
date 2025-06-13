class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Must contain 3 elements
        # The difference betwen any 2 elements is the same

        # left pointer
        left = 0
        # right pointer
        right = 1
        # output
        output = 0
        # count
        count = 0

        # while len(nums) is larger than 3
        while right < len(nums) - 1:
            diff = nums[right] - nums[left]
            while (right < len(nums)-1) and (diff == (nums[right+1] - nums[right])):
                count += 1
                right += 1
            output = output + count
            count = 0
            left += 1
            right = left + 1

        return output