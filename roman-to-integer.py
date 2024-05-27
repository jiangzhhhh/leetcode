class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0
        right = 0
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            cur = mapping[c]
            if cur < right:
                result -= cur
            else:
                result += cur
            right = cur
        return result


s = Solution()
print(s.romanToInt('III'))  # 3
print(s.romanToInt('IV'))  # 4
print(s.romanToInt('LVIII'))  # 58
