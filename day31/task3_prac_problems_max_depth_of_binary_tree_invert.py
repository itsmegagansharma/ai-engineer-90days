"""
Day 31 · Task 3 · Practice: Problems: Max Depth of Binary Tree & Invert Binary Tree

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Max Depth of Binary Tree ----------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def max_depth(root: TreeNode | None) -> int:
    """Recursion: 1 + max(depth of left, depth of right)."""
    pass


# ---------------- Invert Binary Tree ----------------
def invert_tree(root):
    """Swap left and right at every node. Reuse TreeNode from the problem above."""
    pass


def to_list(root):
    return [] if not root else [root.val] + to_list(root.left) + to_list(root.right)


if __name__ == "__main__":
    # Max Depth of Binary Tree
    t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(t) == 3
    # Invert Binary Tree
    t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    assert to_list(invert_tree(t)) == [4, 7, 2, 3, 1]
    print("All tests passed!")
