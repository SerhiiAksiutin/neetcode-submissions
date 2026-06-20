class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while l < len(numbers) - 1 or r < len(numbers):

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target and r < len(numbers) - 1:
                r += 1
            else:
                l = l + 1
                r = l + 1
            print(l < len(numbers) - 1 or r < len(numbers))
            print(numbers[l] + numbers[r] < target and r < len(numbers))
            print(l, r)
        print(l < len(numbers) - 1 or r < len(numbers))
        print(numbers[l] + numbers[r] < target and r < len(numbers))
        print(l, r)
