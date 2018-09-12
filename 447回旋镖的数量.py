class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0        
        for x in points:
            dic = {} 
            for y in points:
                i = x[0] - y[0]
                j = x[1] - y[1]
                dis = i*i+j*j
                dic[dis] = dic.get(dis,0)+1
            for item in dic.values():
                res += item * (item - 1)
        return res