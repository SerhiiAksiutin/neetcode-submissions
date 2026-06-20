class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        l = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)


        for num, count in freq.items():
            l[count].append(num)
        
        res = []
        for i in range(len(l)):
            if len(res) == k:
                return res
            else:
                res += l[~i]