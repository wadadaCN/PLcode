class Solution(object): # rank 65%, O(k+1) extra space.
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = []
        for i in range(rowIndex+1):
            row.append(0)
        row[0] = 1
        for i in range(1,rowIndex+1):
            for j in range(i,0,-1):
                row[j] += row[j-1]
        return row
        
'''
初始[1,0,...,0], k个0, 第一遍[1,1,0,...,0], 第二遍[1,2,1,0,...,0], 第三遍[1,3,3,1,...,0], 也就是把前一遍的右挪一格相加。
'''
