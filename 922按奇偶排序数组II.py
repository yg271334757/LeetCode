class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = [i for i in A if i % 2!= 0]
        even = [j for j in A if j % 2== 0]
        l = len(A)
        res = [0] * l
        for k in range(l):
            if k % 2 == 0:
                res[k] = even.pop()
            else:
                res[k] = odd.pop()
        return res