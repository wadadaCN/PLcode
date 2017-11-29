class Solution: # rank 14%, 用了内置的sort方法，时间复杂度应该是O(m+n)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        nums1.extend(nums2)
        nums1.sort()
        
        if (m + n)%2 == 1:
            return float(nums1[(m+n)//2])
        else:
            return float((nums1[(m+n)//2-1]+nums1[(m+n)//2])/2.0)
            
class Solution: # rank 30%
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
                
 '''
 将A、B切分为左右两部分，左右长度相同，左边最大值小于等于右边最大值，则结束。
 i = (imin + imax) / 2负责二分，j = half_len - i负责确保左右两边长度相同，<i(j)为A(B)左边，>=i(j)为A(B)右边，这解决了第一个条件，左右长度相同。
 imin = i + 1, imax = i - 1一般来说会没有1，直接取当前位置i，但是这样会在某些条件下死循环。
 当i(j) == 0, 说明A(B)所有数都比B[j-1]大，左边全由B中数组成。i(j) == m(n), 同理。
 因为half_len向右偏了半格，如果是奇数，则直接返回max_of_left。
 如果是偶数，再寻找min_of_right。
 '''
