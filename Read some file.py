import os
import sys

bruh = ''
for o in range(len(sys.argv)):
    if '.txt' in sys.argv[o]:
        bruh = sys.argv[o]
file_path = bruh if len(sys.argv) > 1 else None
spis = []
check = []
flag = False
flag_check = False
arg = ['--count', '--num', '--sort']
if not file_path:
    print("ERROR")
    sys.exit(1)

if os.path.isfile(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            spis = [line.rstrip('\n') for line in file]
    for i in range(len(sys.argv)):
        if sys.argv[i] == '--sort':
            spis = sorted(spis)
    for i in range(len(sys.argv)):
        if sys.argv[i] == '--num':
            for k in range(len(spis)):
                check.append(f'{k} {spis[k]}')
            flag_check = True
    for i in range(len(sys.argv)):
        if sys.argv[i] == '--count':
            flag = True
    if flag:
        if flag_check:
            for item in check:
                print(item)
        else:
            for item in spis:
                print(item)
        print(f'rows count: {len(spis)}')
    else:
        if flag_check:
            for item in check:
                print(item)
        else:
            for item in spis:
                print(item)
else:
    print('ERROR')
    sys.exit(1)

# python ReadSomeFile.py --count --sort textX.txt
# mkdir - создание нового каталога(аргумент - название этого каталога)
# cd(change dir)
# cp(copy) (в аргументах указывать файл который копируем и папку куда копировать)
# mv(move)(переименование)
# rm(remove) - удаление и "-r" чтобы удалить всю директорию вместе с содержимым
