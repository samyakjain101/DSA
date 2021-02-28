def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


if __name__ == "__main__":
    root = None
    print(height(root))
