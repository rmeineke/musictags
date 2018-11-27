import os
from music import get_metadata_from_file
from track import Track
from lib.utils import get_path_from_config


def main():
    path = get_path_from_config()
    path = path.strip()

    stray_files = '00_stray_files.txt'
    key_errors = '00_key_errors.txt'
    try:
        os.remove(stray_files)
    except FileNotFoundError as e:
        print(f'strays file not found ... this should continue\n{e}')

    try:
        os.remove(key_errors)
    except FileNotFoundError as e:
        print(f'key error file not found ... this should continue\n{e}')


    for root, dirs, files in os.walk(path):
        for file in files:
            f = os.path.join(root, file)
            _, filetype = os.path.splitext(f)
            if f.lower().endswith('.flac') or f.lower().endswith('.mp3'):
                try:
                    track = get_metadata_from_file(f, filetype)
                    Track.extract_image(track)
                except KeyError as e:
                    with open('00_key_errors.txt', 'a') as f_obj:
                        f_obj.write(f'{f}\n\t{e}\n')
            else:
                with open('00_stray_files.txt', 'a') as f_obj:
                    f_obj.write(f"STRAY: {f}\n")

    print(f'---------------------------------------------------------------------------')
    print(f'ttl_tracks_processed: {Track.ttl_files_processed}')
    print(f'ttl_file_size: {Track.ttl_file_size}')
    print(f'')
    print(f'ttl_png_covers: {Track.ttl_png_covers}')
    print(f'ttl_empty_covers: {Track.ttl_empty_covers}')
    print(f'ttl_oversized_covers: {Track.ttl_oversized_covers}')


if __name__ == '__main__':
    main()
