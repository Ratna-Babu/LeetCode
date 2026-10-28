class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(height)-1

        max_water = 0
        water_area = 0

        while left_pointer<right_pointer:
            length = right_pointer - left_pointer
            water_area = min(height[left_pointer],height[right_pointer]) * length
            if water_area > max_water:
                max_water = water_area
            if height[left_pointer]<height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water
