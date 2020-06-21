class Solution:
    def generateParenthesis(self, n):
        """
        输入：n = 3
        输出：["((()))","(()())","(())()","()(())","()()()"]
        :param n:
        :return:
        """
        # init
        res = []
        def dfs(left_num, right_num, n, str_p):
            # terminate
            if left_num == n and right_num == n:
                res.append(str_p)
                return
            # proccess
            # drill down
            if left_num < n:
                dfs(left_num+1, right_num, n, str_p + '(')
            # add right parenthesis
            if right_num < left_num:
                dfs(left_num, right_num+1, n, str_p + ')')
            
        # prepare for output
        dfs(0, 0, n, '')
        return res


s = Solution()
print(s.generateParenthesis(3))