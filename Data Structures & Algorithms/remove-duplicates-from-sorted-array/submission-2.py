class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1

        while r < len(nums):
            while r < len(nums) and nums[l] == nums[r]:
                r += 1
            if r < len(nums) and nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            print(nums, l)
        return l + 1
