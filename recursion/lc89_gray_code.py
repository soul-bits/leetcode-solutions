from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        self.ans = None
        self.backtrack(n, 0, [0], {0})
        return self.ans

    def backtrack(self, n, cur_num, cur_ans, seen):
        # Terminal
        if len(cur_ans) == 2 ** n:  # n = 2; 2**2 = 4
            self.ans = cur_ans.copy()  # cur_ans is globally shared between recursive calls.
            return True

        for i in range(n):  # n = 2, 0,1
            nxt = cur_num ^ (1 << i)  # 00 ^ 01; 00 ^ 10
            if nxt in seen:
                continue
            cur_ans.append(nxt)
            seen.add(nxt)
            res = self.backtrack(n, nxt, cur_ans, seen)
            if res:
                return True
            seen.remove(nxt)
            cur_ans.pop(-1)
        return False
