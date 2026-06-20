class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        print(res)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        sufix = 1
        for i in range(len(nums)):
            res[~i] *= sufix
            sufix *= nums[~i]
        
        return res
