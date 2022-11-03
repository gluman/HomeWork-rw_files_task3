import os, re

try:
    target = open('target.txt', 'x')
except:
    target = open('target.txt', 'w')

res = []
folder = os.getcwd()
files = os.listdir()
for file in files:
    if '.txt' in file and file != target.name:
        path_to_file = os.path.join(folder, file)
        with open(path_to_file, 'rt', encoding='utf-8') as f:
            rows = []
            count = 0
            for line in f:
                rows.append(line.rstrip('\n'))
                count += 1
            res.append({'file_name': file,
                        'count_rows': count,
                        'rows': rows})
        f.close()

sort_count = sorted(set([d['count_rows'] for d in res]))

for i in sort_count:
    for obj in res:
        if i == obj['count_rows']:
            file_name = obj['file_name']
            count_rows = str(obj['count_rows'])
            target.write(file_name + '\n')
            target.write(count_rows + '\n')
            for line in obj['rows']:
                target.write(line + '\n')
target.close()

