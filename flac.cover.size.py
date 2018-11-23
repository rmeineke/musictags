import os
import logging
import sys
from mutagen.flac import FLAC
from flacfile import FLACFile


def get_path_from_config():
    with open('config.ini', 'r') as cfg:

    return 'test...path'


def main():
    # set up for logging
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL,
              }
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(
            format='%(asctime)s - %(levelname)-8s - %(message)s\n',
            level=level,
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    logger = logging.getLogger(__name__)
    logger.debug('Entering main')

    config = get_path_from_config()
    # path = '/home/robertm/programming/musictags/music'
    # path = '/home/robertm/music'
    print(f'{config}')
    exit(0)

    oversized_covers = []
    missing_covers = []
    png_covers = []
    odd_covers = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith('.flac'):
                f = os.path.join(root, file)
                try:
                    var = FLAC(f)
                    pics = var.pictures
                    if len(pics) == 0:
                        missing_covers.append(f'pic not found: {f}')
                    else:
                        # print(f'{pics}')
                        for p in pics:
                            if p.mime == 'image/png':
                                png_covers.append(f'Found PNG: {f}')
                            if p.type != 3:
                                odd_covers.append(f'Found ODD cover: {p.type} -> {f}')
                            size = sys.getsizeof(p.data)
                            if size > 150000:
                                oversized_covers.append(f'{size} /// {f}')
                            elif size < 10000:
                                # looking for the generic cover ... album.jpg
                                print(f'{size} // this may be the placeholder // {f}')
                except Exception as e:
                    # still not sure what might arise here
                    print(f'{e}')
                    print(f'...................{f}')

                flacfile = FLACFile(f)

    print(f'\n############ Missing Covers')
    for i in missing_covers:
        print(f'{i}')
    print(f'\n############ Oversized Covers')
    for i in oversized_covers:
        print(f'{i}')
    print(f'\n############ Odd Cover Types')
    for i in odd_covers:
        print(f'{i}')
    print(f'\n############ PNG Covers')
    for i in png_covers:
        print(f'{i}')

    print(f'\n')
    print(f'ttl files processed: {FLACFile.ttl_files_processed}')
    print(f'ttl file size: {FLACFile.ttl_file_size:,}')
    print(f'ttl over sized covers: {len(oversized_covers)}')
    print(f'ttl missing covers: {len(missing_covers)}')
    print(f'ttl PNG covers: {len(png_covers)}')
    print(f'ttl ODD cover types: {len(odd_covers)}')
    print(f'\n')


if __name__ == '__main__':
    main()
