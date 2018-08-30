import os


class Track:
    ttl_files_processed = 0
    ttl_file_size = 0

    def __init__(self, file, artist, band, track_title, album_title):
        self.__file = file
        self.__artist = artist
        self.__band = band
        self.__track_title = track_title
        self.__album_title = album_title

        Track.ttl_files_processed += 1
        Track.ttl_file_size += os.path.getsize(file)

    def __str__(self):
        pass
