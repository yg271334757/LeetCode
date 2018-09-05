def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return s
        vowels = 'aeiouAEIOU'
        stack = []
        ans = ''
        for item in s:
            if item in vowels:
                stack.append(item)
        for item in s:
            if item in vowels:
                ans += stack.pop()
            else:
                ans += item
        return ans