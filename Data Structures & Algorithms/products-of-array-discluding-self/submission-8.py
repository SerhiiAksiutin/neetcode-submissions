class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix * res[i]
            prefix *= nums[i]
        print(res)
        postfix = 1
        for i in range(len(nums)):
            res[~i] = postfix * res[~i]
            postfix *= nums[~i]
        print(res)
        return res
