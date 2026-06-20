class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        hash_set = set(nums)

        res = []
        for num in nums:
            if num - 1 not in hash_set:
                sequence = 1
                while num + 1 in hash_set:
                    sequence += 1
                    num += 1
                res.append(sequence)
        return max(res)
    