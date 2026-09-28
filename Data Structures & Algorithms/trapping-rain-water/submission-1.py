class Solution:
    def trap(self, height: List[int]) -> int:
        ## A bar can hold water of height up to the
        ## min(tallest wall on left, tallest wall on right) - its height
        left = 0
        right = len(height) - 1

        water = 0

        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax <= rightMax:
                ## TIP: Imagine leftmax > rightmax, but current left < current right
                ## left side determines the height of the water at left
                left += 1
                if height[left] > leftMax:
                    leftMax = height[left]
                water += leftMax - height[left]
            else:
                right -= 1
                if height[right] > rightMax:
                    rightMax = height[right]
                water += rightMax - height[right]
        return water