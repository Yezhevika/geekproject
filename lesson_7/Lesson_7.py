#import os

# folder = r"/Users/vika/.local/share/virtualenvs/geekproject-TkzCP9jF/lib/python3.8/site-packages/aiohttp"
# py_file = [item for item in os.listdir(folder) if item.lower().endswith(".py")]
# print(py_file)

# folder = r"/Users/vika/.local/share/virtualenvs/geekproject-TkzCP9jF/lib/python3.8/site-packages/django"
# py_file = [item for item in os.listdir(folder) if os.path.isdir(os.path.join(folder, item))]
# print(py_file)

# создание папки
# dir_name = "sample_dir"
# if not os.path.exists(dir_name):
#    os.mkdir(dir_name)

# создание папки с вложенной папкой
# dir_path = os.path.join("data", "src")
# if not os.path.exists(dir_path):
#    os.makedirs(dir_path)

# переименовать папку
# dir_name = "first_dir"
# new_dir_name = "first_new_dir"
# if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
#    os.rename(dir_name, new_dir_name)

# удаление папки в которой есть другие папки/файлы (т е она не пустая)
# import shutil

# to_remove_dir_name = "data"
# if os.path.exists(to_remove_dir_name):
#    shutil.rmtree(to_remove_dir_name)

# копируем файлы из одного в другой и при этом создаем новый файл при помощи shutil и random
# import random
# for _ in range(3):
#   with open('data/hello.txt', encoding='utf-8') as src:
#      with open('data/summary.txt', 'a', encoding='utf-8') as dst:
#           head_size = random.randrange(21)
#           print(head_size, src.read(head_size))
#           shutil.copyfileobj(src, dst)

# копирование информации copy, copy2
import os
from shutil import copyfile, copy, copy2

def show_stat(f_path):
   stat = os.stat(f_path)
   print('{f_p}:\n\tperm - {perm}, modify {m_t:.0f}, access {a_t:.0f}'.format(
       f_p=f_path,
       perm=oct(stat.st_mode),
       m_t=stat.st_mtime,
       a_t=stat.st_atime,
   ))


src = 'data/summary.txt'
show_stat(src)
show_stat(copyfile(src, 'new_data/summary_clone.txt'))
show_stat(copy(src, 'new_data'))
show_stat(copy2(src, 'new_data/summary_clone_2.txt'))