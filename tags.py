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
    for root, dirs, files in os.walk('/home/robertm/programming'):
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

                    if 'TPE1' in meta.keys():
                        track = ftags.tags["TPE1"]
                        print(f'{track}')

                    if 'TPE2' in meta.keys():
                        track = ftags.tags["TPE2"]
                        print(f'{track}')

                    if 'TRCK' in meta.keys():
                        track = ftags.tags["TRCK"]
                        print(f'{track}')

                    if 'TCON' in meta.keys():
                        tcon = ftags.tags["TCON"]
                        print(f'{tcon}')

                    print(f'{type(meta.keys())}')
                    #
                    # if 'APIC:' in meta.keys():
                    #     print(f'Found: APIC:')
                    # elif 'APIC:Cover Art' in meta.keys():
                    #     print(f'Found: APIC:Cover Art')
                    # elif 'APIC:Front cover' in meta.keys():
                    #     print(f'Found: APIC:Front cover')
                    # else:
                    #     print(f'NOT FOUND:::APIC')

                except ID3NoHeaderError as e:
                    print(f' >>> {e} ')

                pic_found = 0
                for k in meta.keys():
                    # print(f'{k}')
                    if k.startswith('APIC'):
                        pic_found = pic_found + 1
                    if k not in tags_found:
                        tags_found.append(k)
                if pic_found:
                    print(f'APIC found')
                else:
                    print(f'>>>>>>>>>>>> appears to be no pic here ?')
    print(f'****************************************************************************')
    print(f'{sorted(tags_found)}')
    # for tag in tags_found:
    #     print(f'{tag} >> {type(tag)}')


if __name__ == '__main__':
    main()


 # if i == 'TIT2':
                    #     st = 'song title: '
                    #     print(f'{st:20} {tags[i]}')
                    # if i == 'TPE1':
                    #     print(f'{tags[i]}')
                    # if i == 'TPE2':
                    #     print(f'{tags[i]}')
                    # if i == 'TALB':
                    #     print(f'{tags[i]}')
                    # if i == 'TPOS':
                    #     print(f'{type(tags[i])}')
                    #     print(f'{tags[i].text}')
                    # if i == 'TRCK':
                    #     print(f'{tags[i]}')
                    # if i == 'TCON':
                    #     print(f'{tags[i]}')
                    # if i == 'TCOM':
                    #     print(f'{tags[i]}')
                    # if i == 'TCOP':
                    #     print(f'tcop >{tags[i]}<')
                    # if i =='TDRC':
                    #     print(f'tdrc >{tags[i]}<')
