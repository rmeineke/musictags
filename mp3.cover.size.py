import os
import logging
import sys
from mp3file import MP3File
from mutagen.id3 import ID3
from mutagen.id3 import ID3NoHeaderError
import mutagen.mp3


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

    oversized_cover = 0
    for root, dirs, files in os.walk('/home/robertm/music'):
        for file in files:
            if file.lower().endswith('.mp3'):
                f = os.path.join(root, file)
                try:
                    meta = ID3(f)
                except ID3NoHeaderError as e:
                    print(f' >>> {e} ')

                data = ''
                tags = mutagen.mp3.Open(f)
                for i in tags:
                    if i.startswith('APIC'):
                        # print(f' # # # # # # # # # # # #')
                        data = tags[i].data
                        if sys.getsizeof(data) > 150000:
                            oversized_cover += 1
                            print(f'{sys.getsizeof(data)} ... {f}')
                        break;
                mp3 = MP3File(f)
    print(f'ttl files processed: {MP3File.ttl_files_processed}')
    print(f'ttl file size: {MP3File.ttl_file_size:,}')
    print(f'ttl over sized covers: {oversized_cover}')


if __name__ == '__main__':
    main()

#
# ttl files processed: 5061
# ttl file size: 42,943,464,128
# ttl over sized covers: 560
#
# ttl files processed: 5061
# ttl file size: 42,942,171,840
# ttl over sized covers: 548
# ttl files processed: 5061
# # ttl file size: 42,932,568,362
# # ttl over sized covers: 457
# ttl files processed: 5061
# ttl file size: 42,912,593,038
# ttl over sized covers: 280