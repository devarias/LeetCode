class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        from sortedcontainers import SortedList
        mod = 10**9+7
        dicti = defaultdict(int)
        s1 = SortedList()
        total = 0
        for i in range(len(instructions)):
            dicti[instructions[i]] += 1
            s1.add(instructions[i])
            if i == 0:
                total = (total + 0) % mod
            else:
                leftIndex = s1.bisect_left(instructions[i])
                small = leftIndex - 0
                big = len(s1) - leftIndex
                if dicti[instructions[i]] > 0:
                    big -= dicti[instructions[i]]
                total = (total + min(small, big)) % mod
        return total
