import logging
import os
import sys

import mutagen.mp3
from mutagen.id3 import ID3
from mutagen.id3 import ID3NoHeaderError

from lib import utils
from mp3file import MP3File


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

    oversized_covers = []
    missing_covers = []

    path = utils.get_path_from_config()
    if len(path) < 8:
        print(f'seems to be something wrong here: {path}')
        exit(1)
    else:
        path = path.strip()

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith('.mp3'):
                f = os.path.join(root, file)
                try:
                    meta = ID3(f)
                except ID3NoHeaderError as e:
                    print(f'{e}')

                pic_not_found = True
                tags = mutagen.mp3.Open(f)
                for i in tags:
                    if i.startswith('APIC'):
                        pic_not_found = False
                        if tags[i].mime == "image/png":
                            print(f'PNG >> {f}')
                        data = tags[i].data
                        size = sys.getsizeof(data)
                        if size > 150000:
                            oversized_covers.append(f'{size} /// {f}')
                        elif size < 10000:
                            # looking for the generic cover ... album.jpg
                            print(f'{size} // this may be the placeholder // {f}')
                        break

                if pic_not_found:
                    missing_covers.append(f'pic not found: {f}')

                mp3 = MP3File(f)

    for i in missing_covers:
        print(f'{i}')
    print(f'\n\n')
    for i in oversized_covers:
        print(f'{i}')

    print(f'\n')
    print(f'ttl files processed: {MP3File.ttl_files_processed}')
    print(f'ttl file size: {MP3File.ttl_file_size:,}')
    print(f'ttl over sized covers: {len(oversized_covers)}')
    print(f'ttl missing covers: {len(missing_covers)}')
    print(f'\n')


if __name__ == '__main__':
    main()
