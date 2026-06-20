class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq)):
            res += freq[~i]
            if len(res) == k:
                return res
