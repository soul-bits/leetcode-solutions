class Solution:
    def permute(self, nums):
        self.ans = []
        def dfs(nums, curr):
            if len(nums) == 0:
                self.ans.append(curr)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], curr + [nums[i]])
        dfs(nums, [])
        return self.ans

s = Solution()
print(s.permute([1,2,3]))