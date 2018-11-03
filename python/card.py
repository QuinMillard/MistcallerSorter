import json

class Card:
    with open('../json/card_color_identities.json', 'r') as f:
        print("[INFO] Loading card data...")
        card_data = json.load(f)
        print("[INFO] Done loading card data.\n")

    @classmethod
    def lookup(klass, names):
        for name in names:
            try:
                color_identity = klass.card_data[name]
                return klass(name, color_identity)
            except KeyError:
                continue

    def __init__(self, name, color_identity):
        self.name = name
        self.color_identity = color_identity
