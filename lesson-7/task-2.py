import os
import yaml


def parce_to_path(obj, _dirs=None, _files=None, addsep=False, path='', sep='\\'):
    if _dirs is None:
        _dirs = []
    if _files is None:
        _files = []

    # для вложенностей добавляем разделитель
    if addsep:
        path += sep

    if type(obj) == dict:
        for key, val in obj.items():
            _dirs.append(f'{path + key}')
            parce_to_path(val, _dirs, _files, True, path + key)

    elif type(obj) == list:
        for el in obj:
            # если в списке находится словарь, транслируем в обработку словарей
            if type(el) == dict:
                parce_to_path(el, _dirs, _files, False, path)

            elif type(el) == str:
                _files.append(f'{path + el}')

    elif type(obj) == str:
        _files.append(obj)

    return _dirs, _files


with open("config.yaml", "r") as f:
    struct = yaml.safe_load(f)

dirs, files = parce_to_path(struct)

for i in dirs:
    os.makedirs(i, exist_ok=True)

for i in files:
    with open(i, "w", encoding="utf-8"):
        pass
