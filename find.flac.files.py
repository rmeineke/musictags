import os
import logging
import sys
from mutagen.flac import FLAC
from flacfile import FLACFile


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

    oversized_covers = 0
    # pic_not_found = True
    for root, dirs, files in os.walk('/home/robertm'):
        # print(f'root: {root}')
        for file in files:
            if file.lower().endswith('.flac'):
                f = os.path.join(root, file)
                p = FLAC(f)
                pics = p.pictures
                if not pics:
                    print(f'no pic found: {f}')
                # print(f'type(pics) == {type(pics)}')
                # print(f'{pics}')
                for i in pics:
                    size = sys.getsizeof(i.data)
                    if size > 150000:
                        print(f'{size:10,} --> {f}')
                        oversized_covers += 1
                        # if i.type == 3:  # front cover
                        #     print(f'found front cover - {i.desc}')
                    #     print(f'sizeof data == {sys.getsizeof(i.data)}')
                    #     with open("cover.jpg", "wb") as f:
                    #         f.write(i.data)

                flac = FLACFile(f)
    print(f'ttl files processed: {FLACFile.ttl_files_processed}')
    print(f'ttl file size: {FLACFile.ttl_file_size:,}')
    print(f'ttl over sized covers: {oversized_covers}')


if __name__ == '__main__':
    main()
