class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(set(chars)) == len(chars):
            return len(chars)
        k = 1
        l = 0
        mark = 0
        for r in range(1,len(chars)):
            if chars[l] == chars[r]:
                k += 1
            elif chars[l] != chars[r]:
                if k == 1:
                    chars[mark] = chars[l]
                    l = r
                    mark += 1
                elif 1 < k <=9:
                    chars[mark] = chars[l]
                    chars[mark + 1] = str(k)
                    mark += 2
                    k = 1
                    l = r
                elif k > 9:
                    chars[mark] = chars[l]
                    for m in range(len(str(k))):
                        chars[mark + m + 1] = str(k)[m]
                    mark += len(str(k)) + 1
                    k = 1
                    l = r
        if r == len(chars) - 1:
            if k == 1:
                chars[mark] = chars[l]
                return mark + 1
            elif 1 < k <=9:
                chars[mark] = chars[l]
                chars[mark + 1] = str(k)
                return mark + 2
            elif k > 9:
                chars[mark] = chars[l]
                for m in range(len(str(k))):
                    mark += m
                    chars[mark + 1] = str(k)[m]
                return mark + len(str(k))