class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        hash_map = {}


        for n in nums:
            hash_map[n] = 1 + hash_map.get(n, 0)

        for num, count in hash_map.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq)):
            if len(res) == k:
                return res
            res += freq[~i]