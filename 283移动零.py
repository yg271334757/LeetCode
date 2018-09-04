class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        'My stupid way, we must use nums[:] instead of nums, or we must make a new list'
        k = nums.count(0)
        nums[:] = [x for x in nums if x != 0]
        nums.extend([0] * k)
        'It\'s a very good method to solve this problem'
        #for i in range(len(nums)):
        #if nums[i]!= 0:
            #nums[idx], nums[i] = nums[i], nums[idx]
            #idx += 1