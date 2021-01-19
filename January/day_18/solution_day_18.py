class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] = counts[n] + 1
            else:
                counts[n] = 1
        for n in counts:
            value = k - n
            if value in counts and counts[value] > 0:
                ops = 0
                if n == k // 2:
                    ops = int(counts[n] // 2)
                else:
                    ops = min(counts[n], counts[value])
                counter += ops
                counts[value] = counts[value] - ops
                counts[n] = counts[n] - ops
        return counter
