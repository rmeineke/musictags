import os
from mutagen.id3 import ID3
from mutagen import File


tags_found = []
for root, dirs, files in os.walk('/home/robertm/music'):
    for file in files:
        if file.endswith('.mp3'):
            f = os.path.join(root,file)
            meta = ID3(f)

            if 'COMM::\x00\x00\x00' in meta.keys():
                ftags = File(os.path.join(root, file))
                comment = ftags.tags['COMM::\x00\x00\x00']
                print(f'{f}\n>>{comment}<<\n')
                # print(f'{f}\n{# meta.keys("COMM::\x00\x00\x00"")}\n\n')

            for k in meta.keys():
                if k not in tags_found:
                    tags_found.append(k)

print(f'{tags_found}')

# (mutagen-Pn3LrErH) [20:08] robertm -- /home/robertm/programming/mutagen $ python tags.py >tags.out.txt
# Traceback (most recent call last):
#   File "tags.py", line 11, in <module>
#     meta = ID3(f)
#   File "/home/robertm/.local/share/virtualenvs/mutagen-Pn3LrErH/lib/python3.6/site-packages/mutagen/id3/_file.py", line 77, in __init__
#     super(ID3, self).__init__(*args, **kwargs)
#   File "/home/robertm/.local/share/virtualenvs/mutagen-Pn3LrErH/lib/python3.6/site-packages/mutagen/id3/_tags.py", line 177, in __init__
#     super(ID3Tags, self).__init__(*args, **kwargs)
#   File "/home/robertm/.local/share/virtualenvs/mutagen-Pn3LrErH/lib/python3.6/site-packages/mutagen/_util.py", line 533, in __init__
#     super(DictProxy, self).__init__(*args, **kwargs)
#   File "/home/robertm/.local/share/virtualenvs/mutagen-Pn3LrErH/lib/python3.6/site-packages/mutagen/_tags.py", line 111, in __init__
#     self.load(*args, **kwargs)
#   File "/home/robertm/.local/share/virtualenvs/mutagen-Pn3LrErH/lib/python3.6/site-packages/mutagen/_util.py", line 169, in wrapper
#     return func(*args, **kwargs)
#   File "/home/robertm/.local/share/virtualenvs/mutagen-Pn3LrErH/lib/python3.6/site-packages/mutagen/_util.py", line 140, in wrapper
#     return func(self, h, *args, **kwargs)
#   File "/home/robertm/.local/share/virtualenvs/mutagen-Pn3LrErH/lib/python3.6/site-packages/mutagen/id3/_file.py", line 150, in load
#     self._header = ID3Header(fileobj)
#   File "/home/robertm/.local/share/virtualenvs/mutagen-Pn3LrErH/lib/python3.6/site-packages/mutagen/_util.py", line 169, in wrapper
#     return func(*args, **kwargs)
#   File "/home/robertm/.local/share/virtualenvs/mutagen-Pn3LrErH/lib/python3.6/site-packages/mutagen/id3/_tags.py", line 66, in __init__
#     raise ID3NoHeaderError("%r doesn't start with an ID3 tag" % fn)
# mutagen.id3._util.ID3NoHeaderError: '/home/robertm/tmp/E4 On Fire.mp3' doesn't start with an ID3 tag
# (mutagen-Pn3LrErH) [20:09] robertm -- /home/robertm/programming/mutagen $ ^C
# (mutagen-Pn3LrErH) [20:14] robertm -- /home/robertm/programming/mutagen $ ^C
# (mutagen-Pn3LrErH) [20:14] robertm -- /home/robertm/programming/mutagen $
