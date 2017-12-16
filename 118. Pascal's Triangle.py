class Solution(object): # rank 80%, 利用列表切片处理n<3情况
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1], [1, 1]]
        if numRows < 3:
            return pascal[:numRows]
        for i in range(2, numRows):
            L = pascal[-1]
            La = [1,]
            for j in range(1,len(L)):
                La.append(L[j] + L[j - 1])
            La.append(1)
            pascal.append(La)
        return pascal
