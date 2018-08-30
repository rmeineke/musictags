import os
from music import evaluate_mp3, evaluate_flac
from track import Track


def main():
    for root, dirs, files in os.walk('/home/robertm/music'):
        for file in files:
            f = os.path.join(root, file)
            print(f'{f}')
            if file.lower().endswith('.flac'):
                print(f'evaluate flac file: {file}')
                evaluate_flac(f)
            elif file.lower().endswith('.mp3'):
                print(f'evaluate mp3 file: {file}')
                track = evaluate_mp3(f)
            else:
                with open('hmmm.txt', 'a') as f_obj:
                    f_obj.write(f"I don't know what to do with this: {file}\n")

    print(f'ttl_tracks_processed: {Track.ttl_files_processed}')
    print(f'ttl_file_size: {Track.ttl_file_size:,}')


if __name__ == '__main__':
    main()
