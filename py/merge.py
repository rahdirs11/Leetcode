class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = len(nums1) - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[last] = nums2[j]
                j -= 1
            else:
                nums1[last] = nums1[i]
                nums1[i] = 0
                i -= 1
            last -= 1

        while j >= 0:
            nums1[last] = nums2[j]
            last -= 1
            j -= 1

