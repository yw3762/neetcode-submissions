# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q:
            pass
        else:
            return False
        dq = deque([q])
        dp = deque([p])
        while dq and dp:
            p_node = dp.popleft()
            q_node = dq.popleft()
            if p_node.val != q_node.val:
                return False
            if p_node.left and q_node.left:
                dq.append(q_node.left)
                dp.append(p_node.left)
            elif not p_node.left and not q_node.left:
                pass
            else:
                return False
            if p_node.right and q_node.right:
                dq.append(q_node.right)
                dp.append(p_node.right)
            elif not p_node.right and not q_node.right:
                pass
            else:
                return False
        return True
        