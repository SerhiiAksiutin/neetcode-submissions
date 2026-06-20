class Solution:
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
                
        