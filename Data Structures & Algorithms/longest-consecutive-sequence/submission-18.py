class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        res = {}

        for num in nums:
            if num - 1 in nums:
                continue
            res[num] = 1
            print(res)
            target = num
            while target + 1 in nums:
                res[num] += 1
                target += 1
        return max(list(res.values()))
