def main():
    n_blocks = int(input()) - 1
    layer = 1
    side_length = 1
    while n_blocks >= (side_length + 2) ** 2:
        side_length += 2
        n_blocks -= side_length ** 2
        layer += 1
    print(layer)


if __name__ == '__main__':
    main()
