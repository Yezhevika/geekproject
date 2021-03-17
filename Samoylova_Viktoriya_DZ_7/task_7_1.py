# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os

dir_path = os.path.join('my_project', 'settings')
if not os.path.exists(dir_path):
   os.makedirs(dir_path)
dir_path = os.path.join('my_project', 'mainapp')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)
dir_path = os.path.join('my_project', 'adminapp')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)
dir_path = os.path.join('my_project', 'authapp')
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

# p_list = {"my_project": ["settings", "mainapp", "adminapp", "authapp"]}
# def make_dir(f_list):
#    for f, f_s in f_list.items():
#       if not os.path.exists(f):
#          for i in range(len(f_s)):
#             os.makedirs(os.path.join(f, f_s[i]))
# make_dir(p_list)

