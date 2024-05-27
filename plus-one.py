from typing import List


class Solution:
    def add_recursion(self, digists: List[int], i: int) -> List[int]:
        n = digists[i]
        if n == 9:
            digists[i] = 0
            if i > 0:
                return self.add_recursion(digists, i-1)
            else:
                return [1] + digists
        else:
            digists[i] = n + 1
        return digists

    def plusOne(self, digits: List[int]) -> List[int]:
        return self.add_recursion(digits, len(digits)-1)


s = Solution()
# print(s.plusOne([1, 2, 3]))
print(s.plusOne([9]))
