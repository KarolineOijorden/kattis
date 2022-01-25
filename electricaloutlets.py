def main():
    for x in range(int(input())):
        numbers = input().split()
        numbers.pop(0)
        sum = 1
        for y in numbers:
            sum += int(y) - 1
        print(sum)


if __name__ == '__main__':
    main()
