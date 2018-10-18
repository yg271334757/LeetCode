class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        maximum=1
        pos = []
        for i in range(len(seats)):
            if seats[i]:
                pos.append(i)
        for i in range(len(pos)-1):
            maximum = max((pos[i]+pos[i+1])//2-pos[i],maximum)
        if seats[len(seats)-1]==0:
            maximum = max(len(seats)-1-pos[-1],maximum)
        if seats[0]==0:
            maximum = max(pos[0]-0,maximum)
        return maximum