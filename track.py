import os
import sys

import random
from shutil import copyfile


def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0, length, 2):
        id += random.choice(number)
        id += random.choice(alpha)
    return id


class Track:
    ttl_files_processed = 0
    ttl_file_size = 0
    ttl_oversized_covers = 0
    ttl_png_covers = 0
    ttl_empty_covers = 0

    def __init__(self, file, artist, band, track_title, album_title, track_num, pic_type, pic_data):
        self.__file = file
        self.__artist = artist
        self.__band = band
        self.__track_title = track_title
        self.__album_title = album_title
        self.__track_num = track_num
        self.__pic_type = pic_type
        self.__pic_data = pic_data

        if sys.getsizeof(self.__pic_data) > 150000:
            Track.ttl_oversized_covers += 1

        if self.__pic_type == 'image/png':
            Track.ttl_png_covers += 1
        elif self.__pic_type == 'EMPTY':
            Track.ttl_empty_covers += 1
        Track.ttl_files_processed += 1
        Track.ttl_file_size += os.path.getsize(file)

    @property
    def track_num(self):
        return self.__track_num

    def __str__(self):
        return f'artist: {self.__artist} // track_title: {self.__track_title}'

    def extract_image(self):
        size = sys.getsizeof(self.__pic_data)
        # pic_type = self.__pic_type
        title = self.__album_title
        title = title.replace(' ', '_')
        title = title.replace('/', '_')
        fn = '/home/robertm/Desktop/mut/' + title + '. ' + random_id(4) + '.jpg'
        if size < 100:
            fn = '/home/robertm/Desktop/mut/' + title + '. ' + random_id(4) + '.png'
            copyfile('x.png', fn)
            return
        with open(fn, 'wb') as output:
            try:
                output.write(self.__pic_data)
            except TypeError as e:
                print(f'{e}')
