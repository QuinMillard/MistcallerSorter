import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class Card:
    FUZZY_MATCH_THRESHOLD = 90

    with open('../json/card_color_identities.json', 'r') as f:
        print("[INFO] Loading card data...")
        card_data = json.load(f)
        print("[INFO] Done loading card data.\n")

    @classmethod
    def lookup(klass, names):
        max_score = klass.FUZZY_MATCH_THRESHOLD
        current_best_card = None
        for name in names:
            fuzzy_matched_name, score = process.extractOne(name, list(klass.card_data.keys()))
            #print("--- BEST MATCH: {}, SCORE: {} ---".format(fuzzy_matched_name, score))
            if score > max_score:
                current_best_card = Card(fuzzy_matched_name, klass.card_data[fuzzy_matched_name])
        return current_best_card

    def __init__(self, name, color_identity):
        self.name = name
        self.color_identity = color_identity
