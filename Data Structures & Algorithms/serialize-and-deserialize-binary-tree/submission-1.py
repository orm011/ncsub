# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    # now implement one that does not blow up in impalanced trees.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # how about a dfs approach. 
        # preorder traversal means we first output the node value 
        # before appending their children and all their own children etc.
        # for an empty tree its None
        # for a single node: why not just val
        # how can we tell apart [val1, null, val2] from [val1, val2, null]
        # append null as placeholder
        # at decode time, how much is missing depends on whether we have 
        # filled up all the children pointers with nulls
        output = []
        pending_nodes = [root]
        while pending_nodes:
            next_node = pending_nodes.pop()
            if next_node:
                output.append(next_node.val)
                pending_nodes.append(next_node.right)
                pending_nodes.append(next_node.left)
            else:
                output.append(None)
        
        return ",".join([str(elt) for elt in output])

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        elts = [int(v) if v!= "None" else None for v in data.split(",")]
        if not elts: # can this happen?
            return None
        elif elts == [None]:
            return None

        # plan: traverse the list. as we find a value, 
        # the next stuff will be descendents. the value is done 
        # when both its pointers are done.
        def _helper(remaining_list: list[int|None]) -> Optional[TreeNode]:
            if remaining_list == []:
                return None, 0
            elif remaining_list[0] is None:
                return None, 1 # offset
            else:
                val = remaining_list[0]
                left, offset1 = _helper(remaining_list[1:])
                right, offset2 = _helper(remaining_list[1+offset1:])
                return TreeNode(val=val, left=left, right=right), 1+offset1+offset2
        
        output, final_offset = _helper(elts)
        return output




        


