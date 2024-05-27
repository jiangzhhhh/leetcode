class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        len1 = len(haystack)
        len2 = len(needle)
        if len2 > len1:
            return -1
        while i < len1 - len2 + 1:
            matched = True
            j = i
            k = 0
            while j < len1 and k < len2:
                if haystack[j] != needle[k]:
                    matched = False
                    break
                j += 1
                k += 1
            if matched:
                return i
            i += 1
        return -1


s = Solution()
print(s.strStr('sadbutsad', 'sad'))  # 0
print(s.strStr('leetcode', 'leeto'))  # -1
print(s.strStr('tsad', 'sad'))  # 1
# print(s.strStr('aaa', 'aaaa'))  # 0
print(s.strStr('mississippi', 'issipi'))  # -1
