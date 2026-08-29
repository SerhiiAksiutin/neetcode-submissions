class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                continue
            else:
                swap = nums[r]
                nums[r] = nums[l]
                nums[l] = swap

                l += 1


        print(nums)
