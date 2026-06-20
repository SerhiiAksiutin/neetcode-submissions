class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counterpart = {}

        for i in range(len(nums)):
            counterpart[target - nums[i]] = i

        for j in range(len(nums)):
            if nums[j] in counterpart and j != counterpart[nums[j]]:
                return [j, counterpart[nums[j]]]