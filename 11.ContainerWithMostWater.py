class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        l, r = 0, len(height)-1
        while l < r:
            currarea = min(height[l], height[r]) * (r-l)
            maximum = max(maximum, currarea)
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l, r = l+1, r-1
        return maximum