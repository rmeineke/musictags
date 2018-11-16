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

    oversized_covers = []
    missing_covers = []
    path = '/home/robertm/programming/musictags/music'
    #path = '/home/robertm/music'
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
                        print(f'{pics}')
                except:
                    print(f'...................{f}')

                flacfile = FLACFile(f)
                # pic_not_found = True
                # tags = mutagen.mp3.Open(f)
                # for i in tags:
                #     if i.startswith('APIC'):
                #         pic_not_found = False
                #         data = tags[i].data
                #         size = sys.getsizeof(data)
                #         if size > 150000:
                #             oversized_covers.append(f'{size} /// {f}')
                #         elif size < 10000:
                #             # looking for the generic cover ... album.jpg
                #             print(f'{size} // this may be the placeholder // {f}')
                #         break
                #
                # if pic_not_found:
                #     missing_covers.append(f'pic not found: {f}')
                #
                # mp3 = MP3File(f)

    print(f'\n')
    print(f'ttl files processed: {FLACFile.ttl_files_processed}')
    print(f'ttl file size: {FLACFile.ttl_file_size:,}')
    print(f'ttl over sized covers: {len(oversized_covers)}')
    print(f'ttl missing covers: {len(missing_covers)}')
    print(f'\n')

    for i in missing_covers:
        print(f'{i}')
    print(f'\n\n')
    for i in oversized_covers:
        print(f'{i}')


if __name__ == '__main__':
    main()
