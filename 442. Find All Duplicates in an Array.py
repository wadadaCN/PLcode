'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''

class Solution(object): # rank 28%, 如果说返回值空间不算的话，不必在最后开辟。当数第二次需要判断时，它是负的，其索引即是所需。
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rList = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                rList.append(abs(i))
            else:
                nums[abs(i) - 1] = -(nums[abs(i) - 1])
        return rList

class Solution(object): # rank 70%, 第一遍得到没出现过的数，其值为正，第二遍对出现的值两次去反，得到重复值。一次循环时可解448
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            nums[abs(i)-1] = -abs(nums[abs(i)-1])
        for i in nums:
            nums[abs(i) - 1] = -(nums[abs(i) - 1])
        return [i+1 for i in range(len(nums)) if nums[i]<0]
