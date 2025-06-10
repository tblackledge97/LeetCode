class Solution(object):
    def findLHS(self, nums):
        """
        Find the longest harmonious subsequence using sliding windows 
        :type nums: List[int]
        :rtype: int
        """
        # sort the array 
        nums.sort()
        # left pointer
        left = 0
        # maximum length of any subsequence found
        max_len = 0

        # move counter right through a sorted array
        for right in range(len(nums)):
            # while the difference is not 1 move the left pointer
            while nums[right] - nums[left] > 1:
                left += 1
            
            # if the difference is 1 increase the length of the
            # max_len
            if nums[right] - nums[left] == 1:
                max_len = max(max_len, right - left + 1)

        return max_len

