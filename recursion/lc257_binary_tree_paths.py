class Solution:
    def binaryTreePaths(self, root):
        self.ans = []
        self.backtrack(root, [])
        return self.ans
    
    def backtrack(self, root, path):
        if root == None: return
        if root.left == None and root.right == None:
            self.ans.append( "->".join( path + [str(root.val)] ) )
            return
        self.backtrack(root.left, path + [str(root.val)])
        self.backtrack(root.right, path + [str(root.val)])
