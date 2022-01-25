from sys import stdin, stdout


def main():
    scores = [sum([int(x) for x in stdin.readline().split()]) for i in range(5)]
    maxn = max(scores)
    stdout.write("{} {}".format(scores.index(maxn) + 1, maxn))


if __name__ == '__main__':
    main()
