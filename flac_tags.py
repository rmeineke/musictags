import os
from mutagen import File


def main():
    tags_found = []
    for root, dirs, files in os.walk('/home/robertm/programming'):
        for file in files:
            if file.endswith('.flac'):
                f = os.path.join(root, file)
                mutobj = File(f, easy=True)
                stray_tags = []
                for i in mutobj:
                    if i not in tags_found:
                        tags_found.append(i)
                    if i == 'title' or i == 'tracknumber' or i == 'albumartist' or i == 'date' \
                            or i == 'tracktotal' or i == 'album' or i == 'artist' or i == 'discnumber':
                        continue
                    else:
                        stray_tags.append(i)
                if stray_tags:
                    print(f'........................................................................')
                    print(f'STRAYS: {f}')
                    for j in stray_tags:
                        print(f'{j}')
    print(f'--------------------------------------------------------')
    print(f'{tags_found}')


if __name__ == '__main__':
    main()


# title
# date
# tracknumber
# albumartist
# tracktotal
# album
# artist
# discnumber