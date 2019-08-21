

def file_to_string(file_locaiton, as_lines=False):
    with open(file_locaiton, 'r') as file:
        if as_lines:
            data = file.read().replace('\n', '')
        else:
            data = file.readline()

    return data