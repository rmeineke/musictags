import os
import sys

import random
from shutil import copyfile
from lib.utils import write_to_logfile


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
    empty_cover_list = []
    oversized_cover_list = []

    def __init__(self, file, artist, band, track_title, album_title, track_num, pic_type, pic_data):
        self.__file = file
        self.__artist = artist
        self.__band = band
        self.__track_title = track_title
        self.__album_title = album_title
        self.__track_num = track_num
        self.__pic_type = pic_type
        self.__pic_data = pic_data

        pic_size = sys.getsizeof(self.__pic_data)
        pic_source = f'{self.__band} -- {self.__album_title}'
        if pic_size > 150000:
            Track.ttl_oversized_covers += 1
            if pic_source not in Track.oversized_cover_list:
                Track.oversized_cover_list.append(pic_source)
        elif pic_size < 500:
            Track.ttl_empty_covers += 1
            if pic_source not in Track.empty_cover_list:
                Track.empty_cover_list.append(pic_source)

        if self.__pic_type == 'image/png':
            Track.ttl_png_covers += 1
            write_to_logfile('00_errors.txt', f'PNG COVER:', f'{self.__file}')
        # elif self.__pic_type == 'EMPTY':
        #     Track.ttl_empty_covers += 1
        #     write_to_logfile('00_errors.txt', f'NO COVER:', f'{self.__file}')

        Track.ttl_files_processed += 1
        Track.ttl_file_size += os.path.getsize(file)

    @property
    def track_num(self):
        return self.__track_num

    def __str__(self):
        return f'artist: {self.__artist} // track_title: {self.__track_title}'

    def extract_image(self):
        size = sys.getsizeof(self.__pic_data)
        title = self.__album_title
        title = title.replace(' ', '_')
        title = title.replace('/', '_')


        # fn = '/home/robertm/Desktop/mut/' + title + '.' + random_id(4) + '.jpg'
        # if size < 100:
        #     fn = '/home/robertm/Desktop/mut/' + title + '.' + random_id(4) + '.png'
        #     copyfile('x.png', fn)
        #     self.empty_cover_list.append(self.__album_title)
        # elif size > 150000:
        #     with open(fn, 'wb') as output:
        #         try:
        #             output.write(self.__pic_data)
        #         except TypeError as e:
        #             print(f'{e}')
