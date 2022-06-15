import os
import json

DIR = r'C:\app\.work\SQL запросы'
curdirpath = os.getcwd()
curdir = curdirpath.split("\\").pop()
file_name = f'{curdir}_summary.json'
file_path = os.path.join(curdirpath, file_name)


content = [os.path.join(root, file) for root, dirs, files in os.walk(DIR) for file in files]

sts = {}
for el in content:
    size = os.stat(el).st_size
    ext = os.path.splitext(el)[1].replace('.', '')
    key = 10 ** len(str(size))

    val = sts.get(key, (0, [],))
    if ext not in val[1]:
        val[1].append(ext)
    val = (val[0] + 1, val[1],)

    sts[key] = val

with open(file_path, 'w', encoding="utf-8") as f:
    f.write(json.dumps(sts))
