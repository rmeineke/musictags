import os


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
        pass
