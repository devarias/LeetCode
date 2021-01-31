class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        dic = defaultdict(list)

        for i in range(m):
            for j in range(n):
                dic[i - j].append(mat[i][j])
        for k in dic:
            dic[k].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = dic[i - j].pop()
        return mat
