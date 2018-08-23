import os

collected_exts = []
for root, dirs, files in os.walk('/home/robertm/programming'):
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        if file_extension not in collected_exts:
            collected_exts.append(file_extension)
print(f'{collected_exts}')