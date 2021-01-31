class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        for n in nums:
            mn = mx = n
            while mn % 2 == 0:
                mn //= 2
            if mx % 2 != 0:
                mx *= 2
            heappush(heap, (mn, mx))
        MX = max([i for i, j in heap])
        output = float('inf')

        while len(heap) == len(nums):
            x, limit = heappop(heap)
            output = min(output, MX-x)
            if x < limit:
                heappush(heap, (x * 2, limit))
                MX = max (MX, x * 2)
        return output
