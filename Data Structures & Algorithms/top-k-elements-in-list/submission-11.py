class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        print(freq)
        for num in nums:
            count[num] = count.get(num, 0) + 1
        print(count)

        for key, value in count.items():
            freq[value].append(key)
        print(freq)

        res = []
        for i in range(len(freq)):
            if freq[~i] and len(res) < k:
                res += freq[~i]
        return res

