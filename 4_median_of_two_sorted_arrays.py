class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        n1, n2 = 0, 0
        m = l1 + l2
        cur_num = 0
        median_nums = []

        # if we had combined sorted array nums of len m = n1 + n2
        # median would be at idx m//2 if m is odd
        # median would be at idx m//2 - 1 and m//2 if m is even
        # hence we need to loop at least till i = m//2 i.e. range(m//2 + 1)
        for i in range(m//2 + 1):
            if n1 < l1:
                if n2 < l2:
                    if nums1[n1] < nums2[n2]:
                        cur_num = nums1[n1]
                        n1 += 1
                    else:
                        cur_num = nums2[n2]
                        n2 += 1
                else:
                    cur_num = nums1[n1]
                    n1 += 1
            elif n2 < l2:
                cur_num = nums2[n2]
                n2 += 1
            if i > m//2 - 2:
                median_nums.append(cur_num)
        
        if m % 2 == 0:
            return sum(median_nums)/2
        else:
            return median_nums[-1]
