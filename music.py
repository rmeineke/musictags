from mutagen.id3 import ID3
from mutagen import File
from track import Track
import sys


def get_artist_from_file(file, filetype):
    if filetype == 'mp3':
        meta = ID3(file)
        return meta['TPE1']
    else:
        mutobj = File(file, easy=True)
        print(mutobj)
        # print(type(mutobj))
        # print(mutobj['albumartist'])
        # print(type(mutobj['albumartist']))
        # print(f'{mutobj["albumartist"][0]}')
        return mutobj["albumartist"][0]

def get_band_from_file(file, filetype):
    if filetype == 'mp3':
        meta = ID3(file)
        return meta['TPE2']
    else:
        mutobj = File(file, easy=True)
        return mutobj["artist"][0]

def get_track_title_from_file(file, filetype):
    if filetype == 'mp3':
        meta = ID3(file)
        return meta['TIT2']
    else:
        mutobj = File(file, easy=True)
        print(f'{mutobj["title"][0]}')
        return mutobj["title"][0]


def get_album_title_from_file(file, filetype):
    if filetype == 'mp3':
        meta = ID3(file)
        return meta['TALB']
    else:
        mutobj = File(file, easy=True)
        print(f'{mutobj["album"][0]}')
        return mutobj["album"][0]


def get_track_num_from_file(file, filetype):
    if filetype == 'mp3':
        meta = ID3(file)
        return meta['TRCK']
    else:
        mutobj = File(file, easy=True)
        print(f'{mutobj["tracknumber"][0]}')
        return mutobj["tracknumber"][0]

def get_cover_data_from_file(file, filetype):
    if filetype == 'mp3':
        mp3 = File(file)
        for i in mp3.tags:
            if i.startswith('APIC'):
                data = mp3.tags[i].data
                print(f'{sys.getsizeof(data)}:\t{file}')
                return data
        print(f'\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nno cover found: {file}')
    else:
        print(f'fetch flac album art')


def evaluate_mp3(file):
    print(f'entering evaluate_mp3: {file}')
    artist = get_artist_from_file(file, 'mp3')
    band = get_band_from_file(file, 'mp3')
    track_title = get_track_title_from_file(file, 'mp3')
    album_title = get_album_title_from_file(file, 'mp3')
    track_num = get_track_num_from_file(file, 'mp3')
    pic_data = get_cover_data_from_file(file, 'mp3')
    return Track(file, artist, band, track_title, album_title, track_num, pic_data)


def evaluate_flac(file):
    print(f'entering evaluate_flac: {file}')
    artist = get_artist_from_file(file, 'flac')
    band = get_band_from_file(file, 'flac')
    track_title = get_track_title_from_file(file, 'flac')
    album_title = get_album_title_from_file(file, 'flac')
    track_num = get_track_num_from_file(file, 'flac')
    pic_data = get_cover_data_from_file(file, 'flac')