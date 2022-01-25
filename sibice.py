from math import sqrt


def main():
    numbers = [int(x) for x in input().split()]
    diagonal = sqrt(numbers[1] ** 2 + numbers[2] ** 2)
    for x in range(numbers[0]):
        if int(input()) > diagonal:
            print('NE')
        else:
            print('DA')


if __name__ == '__main__':
    main()
