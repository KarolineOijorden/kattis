def main():
    n = int(input())
    print(sum([int(input()) for x in range(n)]) - n + 1)


if __name__ == '__main__':
    main()
