class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        hash_set = {}

        for num in nums:
            hash_set[num] = hash_set.get(num, 0) + 1
        print(hash_set)
            
        for key ,val in hash_set.items():
            freq[val].append(key)

        print()
        print(freq)
        res = []
        for i in range(len(freq)):
            if freq[~i] == []:
                continue
            res += freq[~i]
            if len(res) == k:
                return res


