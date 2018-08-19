import os

for root, dirs, files in os.walk('/home/robertm'):
    for file in files:
        if file.lower().endswith('.mp3'):
            f = os.path.join(root, file)
            print(f'{f}')
            print(f'{os.path.getsize(f)}')