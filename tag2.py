import os
import logging
import sys
from mp3file import MP3File
from mutagen.id3 import ID3, TDRC
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
    for root, dirs, files in os.walk('/home/robertm'):
        for file in files:
            if file.lower().endswith('.mp3'):
                f = os.path.join(root, file)
                print(f'******************************************************')
                try:
                    meta = ID3(f)
                except ID3NoHeaderError as e:
                    print(f' >>> {e} ')

                # print(f'{meta.keys()}')
                data = ''
                tags = mutagen.mp3.Open(f)
                # print(f'{tags}')
                # exit(0)
                for i in tags:
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

                    if i.startswith('APIC'):
                        # print(f'found a data tag......')
                        data = tags[i].data
                        if sys.getsizeof(data) > 150000:
                            oversized_cover += 1
                            print(f'{sys.getsizeof(data):12,} ... {f}\n')
                        # print(f'{sys.getsizeof(data)}')
                        # out = open('cover.jpg', 'wb')
                        # out.write(data)
                        # out.close()
                        break;
                mp3 = MP3File(f)

                # print(f'{mp3.file}')

    print(f'ttl files processed: {MP3File.ttl_files_processed}')
    print(f'ttl file size: {MP3File.ttl_file_size:,}')
    print(f'ttl oversized covers: {oversized_cover}')



if __name__ == '__main__':
    main()
#
# tit2 - title/songname
# tpe1 - Lead performer(s)/Soloist(s)
# tpe2 - Band/orchestra/accompaniment
# talb - album
# tpos - part of a set
# trck - track/position
# tcon - content type
# tcom - composer
# tcop - copyright
# tdrc - recording time
