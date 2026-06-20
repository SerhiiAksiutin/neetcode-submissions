class Solution: # nums = [3,4,5,6], target = 7
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            if target - n in hash_map:
                return [hash_map[target - n], i]
            hash_map[n] = i
