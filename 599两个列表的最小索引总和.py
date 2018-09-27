class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = {}
        for i, word in enumerate(list1):
            if word in list2:
                dic[word] = i
        for j, word in enumerate(list2):
            if word in dic:
                dic[word] += j
        k = min(list(dic.values()))
        res = []
        for m in dic:
            if dic[m] == k:
                res.append(m)
        return res