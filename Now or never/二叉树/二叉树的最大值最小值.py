def max_and_min(root):
    if not root:
        return float("inf"), float("-inf")
    left_min, left_max = max_and_min(root.left)
    right_min, right_max = max_and_min(root.right)
    return min(min(left_min, right_min), root.val), max(max(left_max, right_max), root.val)
