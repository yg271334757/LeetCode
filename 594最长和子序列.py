class Solution:
    def findLHS(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        length = 0
        maxL = 0
        for j in dic:
            length = dic[j] + dic.get(j + 1, -dic[j])
            maxL = max(maxL, length)
            length = 0
        return maxL
''' # Counter way
def findLHS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    from collections import Counter
    length=0
    d=dict(Counter(nums))
    for k in d:
        if k-1 in d and d[k]+d[k-1]>length:
            length=d[k]+d[k-1]
    return length
'''