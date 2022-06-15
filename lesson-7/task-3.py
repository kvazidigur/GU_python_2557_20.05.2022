import os
import shutil

ROOT_DIR = 'C:\\GIT\\GU_python_2557_20.05.2022\\lesson-7\\my_project'
DIR_NAME = 'templates'

paths = [root for root, dirs, files in os.walk(ROOT_DIR) if DIR_NAME in dirs and root != ROOT_DIR]

dest = os.path.join(ROOT_DIR, DIR_NAME)
for path in paths:
    src = os.path.join(path, DIR_NAME)
    shutil.copytree(src, dest, dirs_exist_ok=True)
    shutil.rmtree(src)
