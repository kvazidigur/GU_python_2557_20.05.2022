import re

import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
remote_addr_pos = 0
request_type_pos = 5
requested_resource_pos = 6
file_name = 'nginx_logs.txt'

re_log = re.compile(r"(?P<remote_addr>^\S+)\s\S+\s\S+\s\[(?P<request_datetime>.*)\]\s\"(?P<request_type>\w*)\s"
                    r"(?P<requested_resource>[\/\w]+)\s[^\"]+\"\s(?P<response_code>\d+)\s(?P<response_size>\d+)")

# зачитали и сохранили файл
r = requests.get(url=url, timeout=5)
with open(file_name, 'w', encoding='utf-8') as f:
    f.write(r.text)

with open(file_name, 'r', encoding='utf-8') as f:
    for line in f:
        for val in re_log.finditer(line):
            val_dict = val.groupdict()
            val_tuple = tuple(v for k, v in val_dict.items())
            print(val_tuple)
