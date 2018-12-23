import os
import sys

import logbook as logbook

from music import get_metadata_from_file
from track import Track
from lib.utils import get_path_from_config, remove_logfile, write_to_logfile


def main():
    path = get_path_from_config()
    path = path.strip()

    # streamlining down to a single file .... 5 was getting a little awkward
    config_files = ['00_errors.txt']
    for f in config_files:
        remove_logfile(f)

    for root, dirs, files in os.walk(path):
        for file in files:
            f = os.path.join(root, file)
            _, filetype = os.path.splitext(f)
            if filetype == '.flac' or filetype == '.mp3':
                try:
                    track = get_metadata_from_file(f, filetype)
                    Track.extract_image(track)
                except KeyError as e:
                    write_to_logfile('00_errors.txt', f'KEY ERROR: {e}', f'{f}')
            else:
                write_to_logfile('00_errors.txt', f'STRAY FILE:', f'{f}')

    print(f'ttl_tracks_processed: {Track.ttl_files_processed}')
    print(f'ttl_file_size: {Track.ttl_file_size:,}')
    print(f'')
    print(f'ttl_png_covers: {Track.ttl_png_covers}')
    print(f'ttl_empty_covers: {Track.ttl_empty_covers}')
    print(f'ttl_oversized_covers: {Track.ttl_oversized_covers}')


def init_logging(filename: str = None):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = 'Logging initialized.'
    logger = logbook.Logger(f'Startup. Level: {level}')
    logger.notice(msg)


if __name__ == '__main__':
    init_logging()
    main()
