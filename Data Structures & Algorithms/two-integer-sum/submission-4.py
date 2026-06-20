class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_res = {}
        for i, n in enumerate(nums):
            hash_res[target - n] = i

        for i, n in enumerate(nums):
            if n in hash_res and i != hash_res[n]:
                return [i, hash_res[n]]
        