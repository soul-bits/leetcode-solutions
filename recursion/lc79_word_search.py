from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.R = len(board)
        self.C = len(board[0])

        for r in range(self.R):
            for c in range(self.C):
                res = self.backtrack(board, r, c, "", set(), word, 0)
                if res: return res
        return False

    def backtrack(self, board, i, j, cur, visited, target, tgt_ptr):
        if cur == target: return True
        # Boundary Terminal
        if i >= self.R or i < 0 or j >= self.C or j < 0:
            return False
        # Success
        if (i, j) in visited: return False
        if target[tgt_ptr] != board[i][j]: return False
        visited.add((i,j))
        down = self.backtrack(board, i+1, j, cur+board[i][j], visited, target, tgt_ptr+1)
        right = self.backtrack(board, i, j+1, cur+board[i][j], visited, target, tgt_ptr+1)
        up = self.backtrack(board, i-1, j, cur+board[i][j], visited, target, tgt_ptr+1)
        left = self.backtrack(board, i, j-1, cur+board[i][j], visited, target, tgt_ptr+1)
        visited.remove((i,j))
        return down or right or up or left

