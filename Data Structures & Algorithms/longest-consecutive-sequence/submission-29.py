class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)

        res = 0
        for n in nums:
            if n - 1 in hash_set:
                continue
            else:
                longest = 1
                while n + 1 in hash_set:
                    n += 1
                    longest += 1
                res = max(res, longest)
        return res

        