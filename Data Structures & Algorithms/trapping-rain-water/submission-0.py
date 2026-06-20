class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = []

        max_l, max_r = height[l], height[r]
        while not l == r:
            if max_l <= max_r:
                l += 1
                res.append(max(0, max_l - height[l]))
                max_l = max(max_l, height[l])
            else:
                r -= 1
                res.append(max(0, max_r - height[r]))
                max_r = max(max_r, height[r])
            print(res)
        return sum(res)

        