def main():
    pieces = [int(x) for x in input().split()]
    print("{} {} {} {} {} {}".format(1 - pieces[0], 1 - pieces[1], 2 - pieces[2], 2 - pieces[3],
                                     2 - pieces[4], 8 - pieces[5]))


if __name__ == '__main__':
    main()
