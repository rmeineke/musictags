import os
import sys
from mutagen.id3 import ID3
from mutagen.id3 import ID3NoHeaderError
from mutagen import File
import logging


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

    tags_found = []
    for root, dirs, files in os.walk('/home/robertm'):
        for file in files:
            if file.endswith('.mp3'):
                print(f'---------------------------------------------------------------------------')
                f = os.path.join(root, file)
                print(f'{f}')
                try:
                    meta = ID3(f)
                    print(f'{meta.keys()}')

                    ftags = File(os.path.join(root, file))

                    if 'COMM::\x00\x00\x00' in meta.keys():
                        comment = ftags.tags['COMM::\x00\x00\x00']
                        print(f'Comment: >>{comment}<<')

                    if 'TRCK' in meta.keys():
                        track = ftags.tags["TRCK"]
                        print(f'{track}')

                    if 'TCON' in meta.keys():
                        tcon = ftags.tags["TCON"]
                        print(f'{tcon}')

                    if 'APIC:' in meta.keys():
                        print(f'Found: APIC:')
                    elif 'APIC:Cover Art' in meta.keys():
                        print(f'Found: APIC:Cover Art')
                    elif 'APIC:Front cover' in meta.keys():
                        print(f'Found: APIC:Front cover')
                    else:
                        print(f'NOT FOUND:::APIC')

                except ID3NoHeaderError as e:
                    print(f' >>> {e} ')

                for k in meta.keys():
                    if k not in tags_found:
                        tags_found.append(k)

    print(f'****************************************************************************')
    print(f'{sorted(tags_found)}')
    # for tag in tags_found:
    #     print(f'{tag} >> {type(tag)}')


if __name__ == '__main__':
    main()
