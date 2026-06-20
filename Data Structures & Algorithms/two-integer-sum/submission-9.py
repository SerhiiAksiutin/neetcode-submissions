class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            hash_map[target - nums[i]] = i

        print(hash_map)

        for i in range(len(nums)):
            if nums[i] in hash_map.keys() and i != hash_map[nums[i]]:
                return [i, hash_map[nums[i]]] 