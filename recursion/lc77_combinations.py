class Solution:
    def combine(self, n: int, k: int):
        candidates = [i+1 for i in range(n)]
        self.ans = []
        # self.recurse_choose_i([], 0, k, candidates)
        self.recurse_slots([], k, candidates)
        return self.ans

    def recurse_choose_i(self, cur, i, k, candidates):
        if len(cur) == k:
            self.ans.append(cur)
            return
        if i >= len(candidates): return
        self.recurse_choose_i(cur+[candidates[i]], i+1, k, candidates)
        self.recurse_choose_i(cur, i+1, k, candidates)
    
    def recurse_slots(self, cur, k, candidates):
        if len(cur) == k:
            self.ans.append(cur)
            return
        if len(candidates) == 0: return
        for i in range(len(candidates)):
            self.recurse_slots(cur+[candidates[i]], k, candidates[i+1:])
