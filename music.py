from track import Track
from mutagen.id3 import ID3


def get_artist_from_file(file):
    meta = ID3(file)
    return meta['TPE1']


def get_band_from_file(file):
    meta = ID3(file)
    return meta['TPE2']


def get_track_title_from_file(file):
    meta = ID3(file)
    return meta['TIT2']


def evaluate_mp3(file):
    print(f'entering evaluate_mp3: {file}')
    artist = get_artist_from_file(file)
    band = get_band_from_file(file)
    track_title = get_track_title_from_file(file)
    track = Track(file, artist, band, track_title)
    return track


def evaluate_flac(file):
    print(f'entering evaluate_flac: file')
