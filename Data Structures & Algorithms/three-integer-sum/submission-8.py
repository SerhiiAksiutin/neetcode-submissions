class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)

        res = set()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if -nums[i] < nums[l] + nums[r]:
                    r -= 1
                elif -nums[i] > nums[l] + nums[r]:
                    l += 1
                else:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1

        return [list(_) for _ in res]



        