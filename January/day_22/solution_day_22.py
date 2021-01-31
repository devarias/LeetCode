class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = sorted(map(word1.count, set(word2)))
        c2 = sorted(map(word2.count, set(word1)))
        return c1 == c2 and all(c1)
