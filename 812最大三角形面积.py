class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(x,y,z):
            l1 = (abs(x[0]-y[0]) ** 2 + abs(x[1]-y[1]) ** 2) ** 0.5
            l2 = (abs(x[0]-z[0]) ** 2 + abs(x[1]-z[1]) ** 2) ** 0.5
            l3 = (abs(y[0]-z[0]) ** 2 + abs(y[1]-z[1]) ** 2) ** 0.5
            if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1 and l1 - l2 < l3 and l1 - l3 < l2 and l2 - l3 < l1:
                s = (l1+l2+l3)/2
                return (s* (s-l1) * (s-l2) * (s-l3)) ** 0.5
            return 0
        S = 0
        for i in range(len(points) - 2):
            for j in range(i, len(points) - 1):
                for k in range(j, len(points)):
                    A = area(points[i], points[j], points[k])
                    if A > S:
                        S = A
        return S