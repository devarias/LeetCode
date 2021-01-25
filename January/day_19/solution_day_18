class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest, l = "", len(s)
        m = [l - 1]
        for diff in range(1, l):
            m.append(m[0] + diff)
            m.append(m[0] - diff)
        for n in m:
            if min(n + 1, 2 * l - 1 - n) <= len(longest):
                break
            if n % 2 == 0:
                left, right = (n // 2) - 1, (n // 2) + 1
            else:
                left, right = n // 2, (n // 2) + 1
            while left >= 0 and right < l and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len(longest):
                longest = s[left + 1:right]
        return longest
