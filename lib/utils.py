def get_path_from_config():
    with open('config.ini', 'r') as cfg:
        path = cfg.readline()
        return path
