class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = 0
        while(left != right):
            if ((right - left) * self.smallest(height[left], height[right]) > area):
                area = (right - left) * self.smallest(height[left], height[right])            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area
    def smallest(self, v1, v2):
        if v1 >= v2:
            return v2
        else:
            return v1