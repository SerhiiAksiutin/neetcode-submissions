class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        hash_set = set(nums)
        res = []

        for n in nums:
            seq = set()
            if n - 1 not in hash_set:
                seq.add(n)
                k = n
                while k + 1 in hash_set:
                    k += 1
                    seq.add(k)
                res.append(len(seq))

        return max(res)