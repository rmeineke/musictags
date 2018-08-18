import os
import logging
import sys
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

    ttl_files = 0
    for root, dirs, files in os.walk('/home/robertm'):
        for file in files:
            if file.endswith('.mp3'):
                ttl_files += 1
                f = os.path.join(root, file)
                mp3 = MP3File(f)
                print(f'{mp3.name}')
    print(f'ttl_files == {ttl_files}')

if __name__ == '__main__':
    main()