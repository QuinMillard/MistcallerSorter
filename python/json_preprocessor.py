import json
import itertools
import pprint

with open('all_cards.json', 'r') as f:
    data = json.load(f)
    transformed = { k: v['colorIdentity'] for k, v in data.items() }

with open('card_color_identities.json', 'w') as outfile:
    json.dump(transformed, outfile)
