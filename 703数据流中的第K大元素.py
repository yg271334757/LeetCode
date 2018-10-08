class KthLargest:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort(reverse = True)
        self.top_k = nums[:k]
        self.k = k

    def add(self, val):
        if len(self.top_k) == self.k and val <= self.top_k[-1]:   # don't insert val
            return self.top_k[-1]
        
        left, right = 0, len(self.top_k)
        while left < right:   # binary search for insertion point
            
            mid = (left + right) // 2
            if val > self.top_k[mid]:
                right = mid
            else:
                left = mid + 1
            
        self.top_k.insert(left, val)
        if len(self.top_k) > self.k:
            self.top_k.pop()
        return self.top_k[-1]