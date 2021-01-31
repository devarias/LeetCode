class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = ""
        i = n - 1
        while i >= 0:
            a = min(k - i, 26)
            s += chr(a + ord("a") - 1)
            k -= a
            i -= 1
        return s[::-1]
