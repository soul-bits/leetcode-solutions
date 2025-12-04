from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.recursion(target, candidates, [])
        return self.ans

    def recursion(self, target, candidates, cur):
        if target == 0:
            self.ans.append(cur.copy())
            return
        if len(candidates) == 0:
            return
        if target < 0:
            return
        cur.append(candidates[0])
        self.recursion(target - candidates[0], candidates, cur)  # left
        cur.pop(-1)
        self.recursion(target, candidates[1:], cur)  # right

