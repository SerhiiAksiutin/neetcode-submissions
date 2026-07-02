class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        res = 0
        while l < r:
            if height[l] <= height[r]:
                l += 1
                max_l = max(max_l, height[l])
                res += max(0, max_l - height[l])
            else:
                r -= 1
                max_r = max(max_r, height[r])
                res += max(0, max_r - height[r])
            
        
        return res




        