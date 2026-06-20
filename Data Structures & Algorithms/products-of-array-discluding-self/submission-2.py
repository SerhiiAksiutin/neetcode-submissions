class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        print(res)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        print(res)

        sufix = 1
        for i in range(len(nums)):
            res[~i] *= sufix
            sufix *= nums[~i]
        print(res)
        return res
        