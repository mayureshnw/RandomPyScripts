def TOH (n, x, y, z):
    if n > 0:
        TOH (n - 1, x, z, y)
        TOH (n - 1, z, y, x)

TOH (25, 1, 2, 3)
