# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        x_to_y_and_val = defaultdict(list)

        def aux(node, x, y):
            if not node:
                return
            x_to_y_and_val[x].append((-y, node.val))
            aux(node.left, x - 1, y - 1)
            aux(node.right, x + 1, y - 1)

        aux(root, 0, 0)
        result = []
        xs = sorted(x_to_y_and_val.keys())
        for x in xs:
            x_to_y_and_val[x].sort()
            result.append([val for _, val in x_to_y_and_val[x]])
        return result
