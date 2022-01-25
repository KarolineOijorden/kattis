def main():
    numbers = [input() for x in range(int(input()))]
    sum = 0
    for x in numbers:
        sum += int(x[:-1]) ** int(x[-1])
    print(sum)


if __name__ == '__main__':
    main()
