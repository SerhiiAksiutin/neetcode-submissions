class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False