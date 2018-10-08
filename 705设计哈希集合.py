class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = {}
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.a[key] = key
        
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.a:
            self.a.pop(key)

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.a:
            return True
        else:
            return False