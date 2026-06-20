class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        print(freq)

        hash_set = {}
        for n in nums:
            hash_set[n] = 1 + hash_set.get(n, 0)
        print(hash_set)
        for num, cnt in hash_set.items():
            freq[cnt].append(num)
        print(freq)
        res = []
        for i in range(len(freq)):
            for num in freq[~i]:
                res.append(num)
                if len(res) == k:
                    return res
