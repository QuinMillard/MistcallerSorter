from OCR.video_text_recognizer import VideoTextRecognizer
import re
import itertools
import json

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_success(message):
    print(Colors.OKBLUE + message + Colors.ENDC)

def print_failure(message):
    print(Colors.FAIL + message + Colors.ENDC)

def candidate_names(raw_results):
    detected_strings = list(map(lambda str : re.sub(r'\W+', '', str), raw_results))
    permutations = list(itertools.permutations(detected_strings))
    return list(map(lambda x: ' '.join(x), permutations))

def mtg_json_lookup(names):
    with open('card_color_identities.json', 'r') as f:
        cards = json.load(f)

    for name in names:
        try:
            color_identity = cards[name]
            return name, color_identity
        except KeyError:
            continue

for raw_results in VideoTextRecognizer().decode_from_stream():
    print("Raw: {}".format(raw_results))

    candidates = candidate_names(raw_results)
    print("Candidates: {}".format(candidates))

    match = mtg_json_lookup(candidates)

    if match == None:
        print_failure("No match detected.\n")
    else:
        print_success("Matched: {}\n".format(match))
