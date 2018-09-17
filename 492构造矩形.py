class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(area ** 0.5)
        while True:
            if area // w == area / w:
                return [area // w, w]
            w -= 1