import os


class Track():
    ttl_files_processed = 0
    ttl_file_size = 0

    def __init__(self, file, artist, band, track_title):
        self.file = file
        self.artist = artist
        self.band = band
        self.track_title = track_title

        Track.ttl_files_processed += 1
        Track.ttl_file_size += os.path.getsize(file)