class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        # print(nums)    

        res = []
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < -(nums[i]):
                    j += 1
                elif nums[j] + nums[k] > -(nums[i]):
                    k -= 1
                else:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    k -= 1
        return list(res)
            
            
        