import os


def get_base_location():
    pass


def get_config_json():
    os.path.join(os.pardir, 'config.json')


def file_to_string(file_locaiton):
    with open(file_locaiton, 'r') as file:
        data = file.read().replace('\n', '')
    return data
