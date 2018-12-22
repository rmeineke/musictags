import os


def get_path_from_config():
    with open('config.ini', 'r') as cfg:
        path = cfg.readline()
        return path


def cleanup_logfile(file):
    try:
        os.remove(file)
    except FileNotFoundError as e:
        print(f'{file} not found ... this should continue\n{e}')


def write_to_logfile(file, string):
    with open(file, 'w') as log:
        log.write(string)
