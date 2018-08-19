import os


class MP3File():
    ttl_files_processed = 0
    ttl_file_size = 0

    def __init__(self, file):
        self.file = file

        MP3File.ttl_files_processed += 1
        MP3File.ttl_file_size += os.path.getsize(file)