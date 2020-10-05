#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            self.ans += abs(l) + abs(r)
            return node.val + l + r - 1
        
        dfs(root)
        return self.ans
        
# @lc code=end

