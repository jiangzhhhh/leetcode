from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        prefix = ''
        i = 0
        while True:
            if i >= len(strs[0]):
                return prefix
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    return prefix
                if ch != strs[j][i]:
                    return prefix
            prefix += ch
            i += 1


s = Solution()
# print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # fl
# print(s.longestCommonPrefix(["dog", "racecar", "car"]))  #
print(s.longestCommonPrefix(["flower", "flower"]))  #
