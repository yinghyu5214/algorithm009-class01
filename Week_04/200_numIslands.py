class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        # 1. init param, get the row_num, col_num
        row_num = len(grid)
        col_num = len(grid[0])
        lands_num = 0

        # 2. tranverse all the grid
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == '1':
                    lands_num += 1
                    self.dfs(i, j, grid)

        return lands_num

    def dfs(self, i, j, grid):
        row_num = len(grid)
        col_num = len(grid[0])
        # terminator
        if i not in range(0, row_num) or j not in range(0, col_num) or grid[i][j] == '0':
            return
        # process
        grid[i][j] = '0'
        # drill down
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.dfs(i + x, j + y, grid)


s = Solution()
grid = [["1","0","1","1","0","1","1"]]
a = s.numIslands(grid)
print(a)







