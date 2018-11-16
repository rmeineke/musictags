from mutagen.id3 import ID3
from mutagen import File
from mutagen.flac import FLAC
from track import Track
import sys


def get_metadata_from_file(file, filetype):
    # print(f'type: {filetype}')
    if filetype == '.mp3':
        print(f'checking an mp3 file')
        meta = ID3(file)
        artist = meta['TPE1']
        band = meta['TPE2']
        track_title = meta['TIT2']
        album_title = meta['TALB']
        track_num = meta['TRCK']
        pic_data = meta['APIC']
    else:
        print(f'checking a flac file')
        mutobj = File(file, easy=True)
        artist = mutobj["albumartist"][0]
        band = mutobj["artist"][0]
        track_title = mutobj["title"][0]
        album_title = mutobj["album"][0]
        track_num =  mutobj["tracknumber"][0]
        pic_data = ''
        var = FLAC(file)
        pics = var.pictures
        if len(pics) == 0:
            print('----------------------------------------------------')
            print(f'{file}')
            print('has no picture >>>>>>>>>>>')
            print('----------------------------------------------------')
        else:
            print(f'{pics}')
        for p in pics:
            print(f'{p.type}')
            if p.type != 3:
                print(f'\n\n\n >>>>>>>>>{p.type}')

    return Track(file, artist, band, track_title, album_title, track_num, pic_data)


def get_artist_from_file(file, filetype):
    if filetype == 'mp3':
        meta = ID3(file)
        #print(meta['TIT2'])
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
    meta = ID3(file)
    print(type(meta))
    print(meta)
    print(f"rsm >> track title: {meta['TIT2']}")
    print(f"rsm >> album title: {meta['TALB']}")
    print(f"rsm >> track number: {meta['TRCK']}")
    print(f"rsm >> artist: {meta['TPE1']}")
    print(f"rsm >> album artist: {meta['TPE2']}")
    print(f"{meta['APIC']}")

    print('--------------------------------')
    # artist = get_artist_from_file(file, 'mp3')
    # band = get_band_from_file(file, 'mp3')
    # track_title = get_track_title_from_file(file, 'mp3')
    # album_title = get_album_title_from_file(file, 'mp3')
    # track_num = get_track_num_from_file(file, 'mp3')
    # pic_data = get_cover_data_from_file(file, 'mp3')
    return Track(file, artist, band, track_title, album_title, track_num, pic_data)


def evaluate_flac(file):
    print(f'entering evaluate_flac: {file}')
    artist = get_artist_from_file(file, 'flac')
    band = get_band_from_file(file, 'flac')
    track_title = get_track_title_from_file(file, 'flac')
    album_title = get_album_title_from_file(file, 'flac')
    track_num = get_track_num_from_file(file, 'flac')
    pic_data = get_cover_data_from_file(file, 'flac')