from mutagen.id3 import ID3
from mutagen import File
from track import Track


def get_artist_from_file(file):
    meta = ID3(file)
    return meta['TPE1']


def get_band_from_file(file):
    meta = ID3(file)
    return meta['TPE2']


def get_track_title_from_file(file):
    meta = ID3(file)
    return meta['TIT2']


def get_album_title_from_file(file):
    meta = ID3(file)
    return meta['TALB']


def get_track_num_from_file(file):
    meta = ID3(file)
    return meta['TRCK']


def get_cover_data_from_file(file):
    mp3 = File(file)
    for i in mp3.tags:
        if i.startswith('APIC'):
            data = mp3.tags[i].data
            return data


def evaluate_mp3(file):
    print(f'entering evaluate_mp3: {file}')
    artist = get_artist_from_file(file)
    band = get_band_from_file(file)
    track_title = get_track_title_from_file(file)
    album_title = get_album_title_from_file(file)
    track_num = get_track_num_from_file(file)
    pic_data = get_cover_data_from_file(file)
    # with open('cover.jpg', 'wb') as f_obj:
    #     f_obj.write(data)
    return Track(file, artist, band, track_title, album_title, track_num, pic_data)


def evaluate_flac(file):
    print(f'entering evaluate_flac: file')
