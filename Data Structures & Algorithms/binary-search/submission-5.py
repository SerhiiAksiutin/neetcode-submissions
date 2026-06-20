class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        
        def binary_search(l, r, nums, target):
            m = (l + r) // 2
            print(m, nums[m])
            if target == nums[m]:
                return m
            if target < nums[m]:
                return binary_search(l, m - 1, nums, target)
            if target > nums[m]:
                return binary_search(m + 1, r, nums, target)
        return binary_search(0, len(nums) - 1, nums, target)