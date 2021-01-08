class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ""
        string2 = ""
        for word in word1:
            string1 += "".join(word)
        for word in word2:
            string2 += "".join(word)
        if string1 == string2:
            return True
        return False
