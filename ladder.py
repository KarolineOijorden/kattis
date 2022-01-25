from math import tan, radians, ceil, sqrt


def main():
    numbers = [int(x) for x in input().split()]
    a = numbers[0]
    b = a / tan(radians(numbers[1]))
    print(ceil(sqrt(a ** 2 + b ** 2)))


if __name__ == '__main__':
    main()
