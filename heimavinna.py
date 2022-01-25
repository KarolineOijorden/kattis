def main():
    problems = input().split(';')
    n_problems = len(problems)
    for x in problems:
        hyphen = x.find('-')
        if hyphen != -1:
            n_problems += int(x[hyphen+1:]) - int(x[:hyphen])
    print(n_problems)


if __name__ == '__main__':
    main()
