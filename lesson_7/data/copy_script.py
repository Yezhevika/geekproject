import random
import shutil

for _ in range(3):
   with open('data/hello.txt', encoding='utf-8') as src:
       with open('data/summary.txt', 'a', encoding='utf-8') as dst:
           head_size = random.randrange(21)
           print(head_size, src.read(head_size))
           shutil.copyfileobj(src, dst)