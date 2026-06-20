class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqancy = [[] for _ in range(len(nums) + 1)]

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for num, cnt in count.items():
            freqancy[cnt].append(num)
        
        res = []
        for j in range(len(freqancy)):
            if len(res) != k:
                res += freqancy[~j]
            else:
                return res

