class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # largest area
        largest_area = 0
        # current area
        current_area = 0
        # right pointer
        i = 0
        # left pointer 
        j = len(height) - 1

        while i < j:
            
            # calculate the area
            # lowest of the two heights times width
            low_height = min(height[i], height[j])
            
            current_area = low_height * (j-i)                
            # if the new area is larger than previous largest
            largest_area = max(largest_area, current_area)
            
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        
        # return largest stored area
        return largest_area



height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = maxArea(height)
print(result)
    
