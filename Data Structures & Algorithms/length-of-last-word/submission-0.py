class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        n = len(s)

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            i -= 1
            length += 1
        return length

