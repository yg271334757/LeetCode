class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 9
        tenN = 10**n
        for iPlusj  in range(2, int(9*tenN/10+1)):
            upper = tenN - iPlusj
            lower = int(str(upper)[::-1])
            discriminant = iPlusj**2 - 4*lower
            if discriminant >=0:
                root = discriminant**0.5
                j1 = (iPlusj + root) /2
                j2 = (iPlusj - root) /2
                if (j1>0 and abs(j1-int(j1))< 1e-6) or (j2>0 and abs(j2-int(j2))<1e-6):
                    return (upper* tenN+lower)%1337