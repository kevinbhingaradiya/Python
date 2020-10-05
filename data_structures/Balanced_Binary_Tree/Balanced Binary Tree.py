# Checking if a binary tree is CalculateHeight balanced in Python


# CreateNode creation
class CreateNode:

    def __init__(self, item):
        self.item = item
        self.left = self.right = None


# Calculate height
class CalculateHeight:
    def __init__(self):
        self.CalculateHeight = 0


# Check height balance
def is_height_balanced(root, CalculateHeight):

    left_height = CalculateHeight()
    right_height = CalculateHeight()

    if root is None:
        return True

    l = is_height_balanced(root.left, left_height)
    r = is_height_balanced(root.right, right_height)
