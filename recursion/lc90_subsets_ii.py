from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        self.backtrack(nums, 0, [])
        return self.ans

    def backtrack(self, nums, i, cur):
        if i == len(nums):
            self.ans.append(cur)
            return
        self.backtrack(nums, i+1, cur+[nums[i]])
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.backtrack(nums, i+1, cur)

