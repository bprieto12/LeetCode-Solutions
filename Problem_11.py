"""
Container with the most water

Problem:
--------
Given n non-negative integers a1, a2, ..., an, where
each represents a point at coordinate (i, ai). n vertical 
lines are drawn such that the two endpoints of line i is 
at (i, ai) and (i, 0). Find two lines, which together with 
x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Works but it's slow
        maxValue = 0

        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                if area > maxValue: 
                    maxValue = area
        return maxValue

    def betterMaxArea(self, height):
        """
        Idea: the width of a container extends from the first element and ends at the last 
        element.  The height of this container is the smaller of the two heights supporting it.
        For the given height of the container, because we are using the maximum width of the container
        this is the maximum area for this height.  Since we've found the max for this height, we no longer 
        need to look at other areas for this height.  Remove the height, and repeat this process until the
        width of the container is 0.
        """
        start, end = 0, len(height) - 1
        maxContainer = 0

        while start != end:
            maxContainer = max(maxContainer, (end - start) * min(height[start], height[end]))

            if height[start] < height[end]:
                start += 1
            elif:
                end -= 1
    
        return maxContainer

heights = [5, 6, 3, 9]
sol = Solution()
print(sol.maxArea(heights))