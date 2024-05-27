class Solution:
    def nextSpace(self, s: str,  pos: int) -> int:
        length = len(s)
        while pos < length:
            if s[pos] == ' ':
                return pos
            pos += 1
        return length

    def nextLetter(self, s: str, pos: int) -> int:
        length = len(s)
        while pos < length:
            if s[pos] != ' ':
                return pos
            pos += 1
        return length

    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        length = len(s)
        last_word_len = 0
        while i < length:
            i = self.nextLetter(s, i)
            j = self.nextSpace(s, i)
            if i != j:
                word = s[i:j]
                last_word_len = j - i
            i = j
        return last_word_len


s = Solution()
print(s.lengthOfLastWord(' Hllo World'))  # 5
print(s.lengthOfLastWord('   fly me   to   the moon  '))  # 4
