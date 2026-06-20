class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        hash_set = set(nums)

        res = []
        for num in hash_set:
            if num - 1 not in hash_set:
                length = 0
                while num + length in hash_set:
                    length += 1
                longest = max(length, longest)
        return longest
    