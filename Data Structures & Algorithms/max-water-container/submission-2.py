class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for l in range(len(heights)):
            r = l + 1
            while r < len(heights):
                res = max(res, min(heights[l], heights[r]) * (r - l))
                r += 1
        return res



