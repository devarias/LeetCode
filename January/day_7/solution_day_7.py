class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        start, longest = 0, 0
        for i, c in enumerate(s):
            if c in dic and dic[c] >= start:
                start = dic[c] + 1
            else:
                longest = max(longest, i - start + 1)
            dic[c] = i
        return longest
