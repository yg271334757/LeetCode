class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        count = {}
        for i in deck:
            count[i] = count.get(i, 0) + 1
        times = list(count.values())
        mint = min(times)
        while mint >= 2:
            for i in range(len(times)):
                if times[i] % mint != 0:
                    mint -= 1
                    break
                if i == len(times) - 1:
                    return True
        return False