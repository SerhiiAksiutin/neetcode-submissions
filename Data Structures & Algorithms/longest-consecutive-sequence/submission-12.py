class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_set = set(nums)
        res = []
        
        for i in range(len(nums)):
            length = 0
            if nums[i] - 1 not in hash_set:
                length += 1
                curr = nums[i]
                while curr + 1 in hash_set:
                    length +=1
                    curr += 1
                res.append(length)
        return max(res)
        