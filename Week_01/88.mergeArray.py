class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1.直接插入到末尾，然后sort。O(nlongn)
        # 3. 从后往前双指针. O(m+n)
        p1 = m-1
        p2 = n-1
        curr = n+m-1
        while p1>=0 and p2>=0:
            if nums1[p1]>nums2[p2]:
                nums1[curr] = nums1[p1]
                p1 -= 1
            else:
                nums1[curr] = nums2[p2]
                p2 -= 1
            curr -= 1
        if p1<=0:
            nums1[:p2+1] = nums2[:p2+1]