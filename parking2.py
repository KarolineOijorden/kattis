def main():
    for i in range(int(input())):
        input()
        distance = [int(x) for x in input().split()]
        print((max(distance) - min(distance)) * 2)


if __name__ == '__main__':
    main()
