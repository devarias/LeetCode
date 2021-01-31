class Solution:
    def solve(self, mid, m, n, heights):
        q = collections.deque()
        visited = [[False] * n for _ in range(m)]
        q.append((0, 0))
        visited[0][0] = True
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while(q):
            i, j = q.popleft()
            if(i == m - 1 and j == n - 1):
                return True
            for d in dirs:
                x = i + d[0]
                y = j + d[1]
                if(x >= 0 and x < m and y >= 0 and y < n and not visited[x][y]):
                    diff = abs(heights[x][y] - heights[i][j])
                    if(diff <= mid):
                        q.append((x, y))
                        visited[x][y] = True
        return False

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        l = 0
        h = 10 ** 6
        while(l < h):
            mid = l + (h - l) // 2
            if(self.solve(mid, m, n, heights)):
                h = mid
            else:
                l = mid + 1
        return l
