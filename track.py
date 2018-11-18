import os
import random

import random


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

    def __init__(self, file, artist, band, track_title, album_title, track_num, pic_data):
        self.__file = file
        self.__artist = artist
        self.__band = band
        self.__track_title = track_title
        self.__album_title = album_title
        self.__track_num = track_num
        self.__pic_data = pic_data

        Track.ttl_files_processed += 1
        Track.ttl_file_size += os.path.getsize(file)

    @property
    def track_num(self):
        return self.__track_num

    def __str__(self):
        return f'artist: {self.__artist} // track_title: {self.__track_title}'

    def extract_image(self):
        print(f'{self.__album_title}')
        print(f'{self.__artist}')
        title = self.__album_title
        title = title.replace(' ', '_')
        title = title.replace('/', '_')
        fn = '/home/robertm/Desktop/mut/' + title + '.' + random_id(4) + '.jpg'
        print(f'{fn}')
        with open(fn, 'wb') as output:
            output.write(self.__pic_data)




