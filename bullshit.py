import pprint

FILENAME = 'deck_1.csv'

def raw_data_from(file_name):
    f = open(file_name, 'r')
    x = f.read().splitlines()
    f.close()
    return x

def deck_from(lst):
    return { ' '.join(a.split()[1:]) : int(a.split()[0]) for a in lst }


raw_data = raw_data_from(FILENAME)
deck = deck_from(raw_data)
pprint.pprint(deck)
