import os
import sys
from mutagen.id3 import ID3
from mutagen.id3 import ID3NoHeaderError
from mutagen import File
import logging


def main():

    input_tag = input(f"Enter tag: ")
    print(f"Searching for {input_tag}")
    input_tag = input_tag.upper()
    print(f"Searching for {input_tag}")

    # set up for logging
    LEVELS = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(
            format="%(asctime)s - %(levelname)-8s - %(message)s\n",
            level=level,
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    logger = logging.getLogger(__name__)
    logger.debug("Entering main")

    for root, _, files in os.walk("/home/robertm/programming"):
        for file in files:
            f = os.path.join(root, file)
            if file.endswith(".mp3"):
                try:
                    meta = ID3(f)
                    # print(f"{meta.keys()}")

                    ftags = File(os.path.join(root, file))

                    if input_tag in meta.keys():
                        print(f"{f}")
                        tag = ftags.tags[input_tag]
                        print(f"{input_tag}    {tag}")
                        print(
                            f"****************************************************************************"
                        )
                except ID3NoHeaderError as e:
                    print(f" >>> {e} ")
            elif file.endswith(".flac"):
                print(f"FLAC found: {f}")


if __name__ == "__main__":
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
