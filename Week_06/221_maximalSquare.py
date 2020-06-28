class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not len(matrix) or not len(matrix[0]):
            return 0

        maxs = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if not i or not j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxs = max(maxs, dp[i][j])

        maxSquare = maxs * maxs
        return maxSquare
