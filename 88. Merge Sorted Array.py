# You may assume that nums1 has enough space (size that is greater or equal to m + n)
class Solution(object): # rank 95%, 移除多余的0元素，自排序
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while 1:
            if m != len(nums1):
                nums1.remove(0)
            if n != len(nums2):
                nums2.remove(0)
            if m == len(nums1) and n == len(nums2):
                break
        nums1.extend(nums2)
        nums1.sort()

class Solution(object): # 测试不通过，但是pycharm没问题，虽然这段代码本身不满足nums1内排序的要求，引入了num，地址变了，恶心。
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        num = []
        while 1:
            if i == m:
                num.extend(nums2[j:n])
                break
            if j == n:
                num.extend(nums1[i:m])
                break
            if nums1[i] < nums2[j]:
                num.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                num.append(nums2[j])
                j += 1
            else:
                num.append(nums1[i])
                num.append(nums2[j])
                i += 1
                j += 1
        nums1 = num[:]
        return nums1

class Solution(object): # rank 56%
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
 
 '''
 nums1足够大，可以将大的放在最后，若nums1先读完，则nums2剩下的组成nums1前部
 '''
