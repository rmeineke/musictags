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

    for root, dirs, files in os.walk('/home/robertm'):
        for file in files:
            if file.lower().endswith('.mp3'):
                f = os.path.join(root, file)

                try:
                    meta = ID3(f)
                except ID3NoHeaderError as e:
                    print(f' >>> {e} ')

                print(f'{meta.keys()}')
                data = ''
                tags = mutagen.mp3.Open(f)
                # print(f'{tags}')
                # exit(0)
                for i in tags:
                    if i.startswith('APIC'):
                        print(f'found a data tag......')
                        data = tags[i].data
                        break;
                out = open('cover.jpg', 'wb')
                out.write(data)
                out.close()
                mp3 = MP3File(f)

                print(f'{mp3.file}')

    print(f'ttl files processed: {MP3File.ttl_files_processed}')
    print(f'ttl file size: {MP3File.ttl_file_size:,}')


if __name__ == '__main__':
    main()