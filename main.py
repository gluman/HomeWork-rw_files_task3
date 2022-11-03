import os, re
try:
    target = open('target.txt', 'x')
except:
    target = open('target.txt', 'w')
res = []
folder = os.getcwd()
files = os.listdir()
for file in files:
    if '.txt' in file:
        path_to_file = os.path.join(folder, file)
        with open(path_to_file, 'rt', encoding='utf-8') as f:
            rows = []
            for line in f:
                rows.append(line.rstrip('\n'))
            res.append({'file_name': file,
                        'count_rows': len(f.readlines()),
                        'rows': rows})

print(res)