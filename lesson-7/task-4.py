import os

DIR = r'C:\app\.work\SQL запросы'

content = [os.path.join(root, file) for root, dirs, files in os.walk(DIR) for file in files]
print(content)

sts = {}
for el in content:
    size = os.stat(el).st_size
    key = 10 ** len(str(size))
    sts[key] = sts.get(key, 0) + 1

print(sts)
