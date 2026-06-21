class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)

        res = 0
        for n in nums:
            longest = [n]
            while n + 1 in hash_set:
                n += 1
                longest.append(n)
            res = max(res, len(longest))
        return res

        