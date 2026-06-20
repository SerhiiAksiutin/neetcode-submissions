class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 0
        nums = set(nums)

        for num in nums:
            length = 1
            if num - 1 in nums:
                continue
            else:
                while num + 1 in nums:
                    length += 1
                    num += 1
            res = max(res, length)
        return res

    