class Solution(object): # rank 70%, 
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        aDict = {}
        maxLen = 0
        minLen = len(nums)
        maxList = []
        for i in range(len(nums)):
            aDict.setdefault(nums[i],[0,i])
            aDict[nums[i]][0] += 1
            if len(aDict[nums[i]]) == 2:
                aDict[nums[i]].append(i)
            else:
                aDict[nums[i]][2] = i
            if maxLen <= aDict[nums[i]][0]:
                maxLen = aDict[nums[i]][0]
                maxList.append(nums[i])
        for i in range(len(maxList)-1,-1,-1):
            if aDict[maxList[i]][0] != maxLen:
                return minLen
            try:
                length = aDict[maxList[i]][2] - aDict[maxList[i]][1] + 1
                if minLen > length:
                    minLen = length
            except:
                return minLen
            if i == 0:
                return minLen

'''
时间复杂度O(N)，相当于遍历了nums两遍。空间复杂度O(N)，相当于存了两个nums，其中还记录了每个元素的位置。
思路：第一遍遍历，获得最多出现数信息；第二遍遍历，把之前记录的曾经的最多出现数检查一遍，记录其中最短的序列长度。其中try是针对aDict[maxList[i]][2]
索引超出，说明所有数都只出现了一遍。
'''

class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans

'''
来自Solution，思路与我一样，存储方式不同，使用max与min两个内建函数提高速度，减少了额外的存储空间。
'''
