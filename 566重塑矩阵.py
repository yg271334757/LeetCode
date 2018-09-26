class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums[0]) * len(nums) != r * c:
            return nums
        tem = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                tem.append(nums[i][j])
        res = []
        for k in range(r):
            ans = [0] * c
            for l in range(c):
                ans[l] = tem[k * c + l]
            res.append(ans)
        return res