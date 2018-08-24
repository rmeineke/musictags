import os


class FLACFile():
    ttl_files_processed = 0
    ttl_file_size = 0

    def __init__(self, file):
        self.file = file

        FLACFile.ttl_files_processed += 1
        FLACFile.ttl_file_size += os.path.getsize(file)