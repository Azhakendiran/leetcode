class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the shorter array to keep bounds safe and fast
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2

        low, high = 0, m
        while low <= high:
            cut1 = (low + high) // 2  # elements from nums1 in left half
            cut2 = total_left - cut1  # elements from nums2 in left half

            left1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            right1 = float("inf") if cut1 == m else nums1[cut1]

            left2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
            right2 = float("inf") if cut2 == n else nums2[cut2]

            if left1 <= right2 and left2 <= right1:
                # Valid partition found
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                # Too many elements taken from nums1; move left
                high = cut1 - 1
            else:
                # Too few elements taken from nums1; move right
                low = cut1 + 1

        return 0.0