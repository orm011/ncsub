# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# iterative traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        pending_nodes = [(root, "pre")]
        # two states "pre" and "now" indicating if expanding work or doing work.
        while pending_nodes:
            next_node, state = pending_nodes.pop()
            if not next_node: # null is skipped
                continue
            elif state == "now":
                ans.append(next_node.val)
                pending_nodes.append((next_node.right, "pre"))
            elif state == "pre":
                pending_nodes.append((next_node, "now"))
                pending_nodes.append((next_node.left, "pre"))

        return ans


