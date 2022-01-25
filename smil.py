def main():
    line = input()
    for i in range(1, len(line)):
        if line[i] == ')':
            symbol = line[i-1]
            if symbol == '-' and i > 1:
                eye = line[i-2]
                if eye == ':' or eye == ';':
                    print(i-2)
            elif symbol == ':' or symbol == ';':
                print(i-1)


if __name__ == '__main__':
    main()
