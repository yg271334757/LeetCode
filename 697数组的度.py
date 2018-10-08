class Solution:
    def findShortestSubArray(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in range(len(nums)):#TLE if i use the "get" Function
            if nums[i] in count:
                count[nums[i]] += [i]
            else:
                count[nums[i]] = [i]
        maxL = len(max(count.values(), key = lambda x: len(x)))
        a = float('inf')
        for j in count:
            if len(count[j]) >= maxL:
                maxL = len(count[j])
                minL = count[j][-1] - count[j][0] + 1
                if minL < a:
                    a = minL
        return a