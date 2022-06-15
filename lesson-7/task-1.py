import os

struct = [

    ('my_project',),
    ('my_project', 'settings'),
    ('my_project', 'mainapp'),
    ('my_project', 'adminapp'),
    ('my_project', 'authapp')
]

if __name__ == "__main__":
    for el in struct:
        try:
            os.mkdir('/'.join(el))
        except FileExistsError as e:
            pass
