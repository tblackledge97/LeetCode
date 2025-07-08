class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m = len(nums1)
        n = len(nums2)
        
        # Initialize the DP table with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        max_len = 0
        
        # Fill the DP table from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    max_len = max(max_len, dp[i][j])
        
        return max_len