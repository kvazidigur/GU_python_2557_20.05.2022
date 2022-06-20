import re


def email_parse(email):
    re_username = re.compile(r'.+(?=@)')
    re_domain = re.compile(r'(?<=@)[\w+_-]+\.\w+$')

    email_dict = {'username': re.search(re_username, email.strip()), 'domain': re.search(re_domain, email.strip())}
    if email_dict['username'] is None or email_dict['domain'] is None:
        raise ValueError(f'wrong email: {email}')
    else:
        email_dict['username'] = email_dict.get('username').group(0)
        email_dict['domain'] = email_dict.get('domain').group(0)

    return email_dict


print(email_parse('someone@geekbrains.ru'))
