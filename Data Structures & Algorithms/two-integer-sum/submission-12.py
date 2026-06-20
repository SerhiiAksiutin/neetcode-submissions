class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        counterpart = {}
        for i in range(len(nums)):
            counterpart[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in counterpart and i != counterpart[nums[i]]: # 3 in [4,3,2,1] and 0 != 1
                return [i, counterpart[nums[i]]]
        
