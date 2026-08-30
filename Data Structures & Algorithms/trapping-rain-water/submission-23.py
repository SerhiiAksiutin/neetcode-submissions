class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        res = 0
        max_l, max_r = height[l], height[r]
        while l < r:
            # print(f"for index {l} max_l is {max_l} and for index {r} max_r is {max_r}")
            if max_l < max_r:
                l += 1
                max_l = max(height[l], max_l)
                res += max(max_l - height[l], 0)
                # print(f"collected water: {res} \n > moved left"),
            else:
                r -= 1
                max_r = max(height[r], max_r)
                res += max(max_r - height[r], 0)
                # print(f"collected water: {res} \n < moved right")
                
        return res

        