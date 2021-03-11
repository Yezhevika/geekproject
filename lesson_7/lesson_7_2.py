num = input("Enter number: ")
try:
    num = int(num)
except ValueError as err:
    print(err)
else:
    print(num)
finally:
    print("I`m")


f_path = 'new_one.txt'
try:
   with open(f_path, 'r', encoding='utf-8') as f:
       content = f.read()
   print(content)
except (FileNotFoundError, EOFError) as e:
   print(f'concrete error: {e}')
except Exception as e:
   print(f'global error: {e}')