class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for n in nums:
            if n not in hash_set:
                hash_set.add(n)
            else:
                return True
        return False


            