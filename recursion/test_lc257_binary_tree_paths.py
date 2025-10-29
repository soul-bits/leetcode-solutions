import unittest

# Define TreeNode for testing
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Import the solution class
from recursion.lc257_binary_tree_paths import Solution  # <-- change to the actual filename if needed

class TestBinaryTreePaths(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_single_node(self):
        root = TreeNode(1)
        expected = ["1"]
        self.assertEqual(self.sol.binaryTreePaths(root), expected)

    def test_two_levels(self):
        #    1
        #   / \
        #  2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        expected = ["1->2", "1->3"]
        result = self.sol.binaryTreePaths(root)
        self.assertCountEqual(result, expected)

    def test_three_levels_left_heavy(self):
        #     1
        #    /
        #   2
        #  /
        # 3
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        expected = ["1->2->3"]
        self.assertEqual(self.sol.binaryTreePaths(root), expected)

    def test_mixed_tree(self):
        #       1
        #      / \
        #     2   3
        #      \
        #       5
        root = TreeNode(1)
        root.left = TreeNode(2, None, TreeNode(5))
        root.right = TreeNode(3)
        expected = ["1->2->5", "1->3"]
        result = self.sol.binaryTreePaths(root)
        self.assertCountEqual(result, expected)

    def test_empty_tree(self):
        self.assertEqual(self.sol.binaryTreePaths(None), [])

if __name__ == "__main__":
    unittest.main()
