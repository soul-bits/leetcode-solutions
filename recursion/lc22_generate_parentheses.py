class Solution:
    def generateParenthesis(self, n):
        self.ans = []
        self._recursion(cur="", open_count=0, close_count=0, n=n)
        return self.ans

    def _recursion(self, cur, open_count, close_count, n):
        if close_count > open_count:
            return
        if close_count > n or open_count > n:
            return
        if close_count == n and open_count == n:
            self.ans.append(cur)
            return
        self._recursion(cur + "(", open_count + 1, close_count, n)
        self._recursion(cur + ")", open_count, close_count + 1, n)


