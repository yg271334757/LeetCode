class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 1:
            return grid[0][0] + grid[0][0] + 1
        nos = 0
        for i in grid:
            nos += i.count(0)
        sxy = len(grid) * len(grid[0]) - nos
        sxz = sum(map(max, grid))
        syz = sum(map(max, list(zip(*grid))))
        return sxy + sxz + syz