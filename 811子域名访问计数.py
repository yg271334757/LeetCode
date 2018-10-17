class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        times = []
        domain = []
        for i in cpdomains:
            a = i.split()
            times.append(int(a[0]))
            domain.append(a[1])
        dictmap = {}
        for j, value in enumerate(domain):
            if value not in dictmap:
                dictmap[value] = times[j]
            else:
                dictmap[value] += times[j]
        res = {}
        for m in dictmap.keys():
            a = m.split('.')
            for _ in range(m.count('.')+1):
                k = '.'.join(a)
                if k in res:
                    res[k] += dictmap[m]
                else:
                    res[k] = dictmap[m]
                a.pop(0)
        ans = []
        for d in res:
            s = '{0} {1}'.format(res[d], d)
            ans.append(s)
        return ans       