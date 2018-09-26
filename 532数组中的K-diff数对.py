class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or len(nums)==0:
            return 0
        count_dict = {}
        count = 0
        for num in nums:
            count_dict[num] = count_dict.get(num,0) + 1			
        for key in count_dict:
            if k:
                if key + k in count_dict:
                    count += 1
            else:
                if count_dict[key] >= 2:
                    count += 1
        return count