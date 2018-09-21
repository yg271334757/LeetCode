#class Solution:
    #def findRelativeRanks(self, nums):
        #"""
        #:type nums: List[int]
        #:rtype: List[str]
        #"""
        #tem = nums.copy()
        #tem.sort(reverse = True)
        #rank = []
        #for i in nums:
            #rank.append(tem.index(i))
        #for j in range(len(rank)):
            #if rank[j] == 0:
                #rank[j] = "Gold Medal"
            #elif rank[j] == 1:
                #rank[j] = "Silver Medal"
            #elif rank[j] == 2:
                #rank[j] = "Bronze Medal"
            #else:
                #rank[j] = str(rank[j] + 1)
        #return rank
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        newnums = sorted(nums, reverse = True)
        dic = {}
        l = len(newnums)
        dic[newnums[0]] = 'Gold Medal'
        if l > 1:
            dic[newnums[1]] = 'Silver Medal'
        if l > 2:
            dic[newnums[2]] = 'Bronze Medal'
        for i in range(3, l):
            dic[newnums[i]] = str(i + 1)
        res = []
        for j in nums:
            res.append(dic[j])
        return res