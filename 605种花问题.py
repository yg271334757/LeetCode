class Solution:
    def canPlaceFlowers(self,flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ''' # count how many 0 between two 1
        def canPlaceFlowers(self, flowerbed, n):
            p = 0
            c = 1
            for flower in flowerbed:
                if flower:
                    p += (c - 1) // 2
                    c = 0
                else:
                    c += 1     
            p += c // 2        
            return p >= n
        '''
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):            
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0: 
                    return True
        return False 
