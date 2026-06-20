class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:

    #     if nums == []:
    #         return 0
    #     res = {}

    #     for num in nums:
    #         if num - 1 in nums:
    #             continue
    #         res[num] = 1
    #         print(res)
    #         target = num
    #         while target + 1 in nums:
    #             res[num] += 1
    #             target += 1
    #     return max(list(res.values()))
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        hash_set = set(nums)
        
        res = []
        for n in nums:
            seq = []
            if n - 1 not in hash_set:
                seq.append(n)
                while n + 1 in hash_set:
                    n += 1
                    seq.append(n)
                res.append(len(seq))
        return max(res)
