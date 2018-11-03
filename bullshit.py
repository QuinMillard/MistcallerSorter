import pprint

def read_files(file_name):
    f = open(file_name, 'r')
    x = f.read().splitlines()
    f.close()
    return x

pprint.pprint(read_files('deck_1.csv'))
