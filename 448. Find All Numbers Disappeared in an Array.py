'''Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.'''

class Solution(object): rank 57%, 因为没有出现的数不会影响列表相应索引的值，所以将出现的数作为索引的值全置为负，最后返回正值对应索引（+1）的列表
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            nums[abs(i)-1] = -abs(nums[abs(i)-1])
        return [i+1 for i in range(len(nums)) if nums[i] > 0]

class Solution(object): # rank 82%, 集合差集，但是用了额外空间
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rNums = [i for i in range(1,len(nums)+1)]
        return list(set(rNums)-set(nums))
        
