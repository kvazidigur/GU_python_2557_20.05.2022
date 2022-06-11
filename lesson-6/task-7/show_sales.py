import sys
FILENAME = 'sales.txt'

if __name__ == "__main__":
    sales = ''
    with open(FILENAME, 'r', encoding='utf-8') as f:
        if len(sys.argv) == 1:
            sales = f.read()
        elif len(sys.argv) == 2 and sys.argv[1].isdigit():
            for i, line in enumerate(f, 1):
                if i >= int(sys.argv[1]):
                    sales = line
        elif len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
            for i, line in enumerate(f, 1):
                if int(sys.argv[1]) <= i <= int(sys.argv[2]):
                    sales += line
                elif i > int(sys.argv[2]):
                    break

    exit(print(sales))
