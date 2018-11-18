import os
from music import get_metadata_from_file
from track import Track


def main():
    print(f'\nChoose path:\n')
    print(f'1: path1 = /home/robertm/programming/musictags/music')
    print(f'2: path2 = /home/robertm/music')
    resp = int(input())
    path = ''
    if resp == 1:
        path = '/home/robertm/programming/musictags/music'
    elif resp == 2:
        path = '/home/robertm/music'
    else:
        exit(0)

    for root, dirs, files in os.walk(path):
        for file in files:
            f = os.path.join(root, file)
            # print(f'file: {file}')
            # print(f'f: {f}')
            _, filetype = os.path.splitext(f)
            if f.lower().endswith('.flac') or f.lower().endswith('.mp3'):
                # print(f'evaluate: {file}')
                try:
                    track = get_metadata_from_file(f, filetype)
                    # print(f'{track}')
                    Track.extract_image(track)
                except KeyError as e:
                    with open('00_key_errors.txt', 'a') as f_obj:
                        f_obj.write(f'{f}\n\t{e}\n')
            else:
                with open('00_stray_files.txt', 'a') as f_obj:
                    print(f'stray: {file}')
                    f_obj.write(f"I don't know what to do with this:\n\t{f}\n")

    print(f'ttl_tracks_processed: {Track.ttl_files_processed}')
    print(f'ttl_file_size: {Track.ttl_file_size:,}')


if __name__ == '__main__':
    main()
