class Solution(object): # rank 70%, 效率不高
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        aSet = {'0','10','11'}
        i = 0
        while len(bits) > 1:
            if str(bits[i])+str(bits[i+1]) in aSet:
                i += 2
                if i == len(bits)-1:
                    return True
                elif i == len(bits):
                    return False
            else:
                i += 1
                if i == len(bits)-1:
                    return True
        return True
        
class Solution(object): # rank 82%, 参考的Solution，思路与上一段类似，都是遇0进一位，遇1进2位，效率不高
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits)-1:
            i += bits[i] + 1
        return i == len(bits) - 1
 
 class Solution(object): # rank 18%, 参考的Solution
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0
        
'''
最后一个Solution快在两处，一处是只有最坏情况才需要完全遍历，一处是使用了位运算。
思路：最后两个0（如果存在）之间必需要有偶数个1，因此，当bits pop出倒数第二个0时，循环停止，bits最后一位与之间的若干个1抑或运算，如果最后一位是0，
则偶数个1使得最后异或结果为0，满足输出要求；如果最后一位是1，要输出true，则需要奇数个1，，，，，嗯，所以[0,1,1,1,1]它返回true，实际应该是false，
这算法不行。
嗯，题目说给定数据以0结尾，前面分析错了。
'''
