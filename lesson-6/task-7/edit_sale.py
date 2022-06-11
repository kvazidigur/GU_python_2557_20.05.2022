import sys
FILENAME = 'sales.txt'

if __name__ == "__main__":
    salesum = sys.argv[1]
    lnum = int(sys.argv[2])
    with open(FILENAME, 'r+', encoding='utf-8') as f:
        i = 1
        lpos = f.tell()
        line = f.readline()
        while line:
            if i == lnum:
                break
            lpos = f.tell()
            line = f.readline()
            i += 1
        else:
            exit('Указаная строка не существует')

        f.seek(lpos)
        f.write(salesum)
