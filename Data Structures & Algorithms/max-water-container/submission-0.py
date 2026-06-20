class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res =[]

        while l < r:
            print(l, r)
            if heights[l] <= heights[r]:
                res.append(heights[l] * (r - l))
                l += 1
            else:
                res.append(heights[r] * (r - l))
                r -= 1
        return max(res)

