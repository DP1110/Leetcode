class Solution(object):
    def recoverTree(self, root):
        first = second = prev = None
        curr = root

        while curr:
            if curr.left is None:
                # visit curr
                if prev and prev.val > curr.val:
                    if first is None:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                # find inorder predecessor
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right

                if pred.right is None:
                    pred.right = curr  # create thread
                    curr = curr.left
                else:
                    pred.right = None  # remove thread
                    # visit curr
                    if prev and prev.val > curr.val:
                        if first is None:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right

        first.val, second.val = second.val, first.val