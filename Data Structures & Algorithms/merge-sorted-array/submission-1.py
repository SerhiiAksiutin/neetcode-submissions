class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = m - 1, len(nums1) - 1
        k = n - 1

        while k >= 0:
            print(nums1[l], "vs", nums2[k], "in", r)
            if nums2[k] > nums1[l] or l < 0:
                nums1[r] = nums2[k]
                r -= 1
                k -= 1
            else:
                nums1[r] = nums1[l]
                r -= 1
                l -= 1
            print(nums1, "while", l, "and", k)
