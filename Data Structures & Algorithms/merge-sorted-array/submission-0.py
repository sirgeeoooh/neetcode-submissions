class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p_nums1 = m - 1
        p_nums2 = n - 1
        p_nums1_end = m + n - 1
        while p_nums1 >= 0 and p_nums2 >= 0:
            if nums1[p_nums1] > nums2[p_nums2]:
                nums1[p_nums1_end] = nums1[p_nums1]
                p_nums1 -= 1
            else:
                nums1[p_nums1_end] = nums2[p_nums2]
                p_nums2 -= 1
            p_nums1_end -= 1

        nums1[:p_nums2 + 1] = nums2[:p_nums2 + 1]