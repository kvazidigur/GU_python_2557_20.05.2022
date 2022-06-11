import sys
FILENAME = 'sales.txt'

if __name__ == "__main__":
    salesum = sys.argv[1]
    with open(FILENAME, 'a', encoding='utf-8') as f:
        f.write(f'{salesum}\n')
