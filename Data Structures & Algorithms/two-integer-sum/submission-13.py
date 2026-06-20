class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            counterpart = target - nums[i]
            if counterpart in hash_map:
                return [hash_map[counterpart], i]
            else:
                hash_map[nums[i]] = i