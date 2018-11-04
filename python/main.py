from OCR.video_text_recognizer import VideoTextRecognizer
from card import Card
from rule import Rule
from bin_controller import BinController
import re
import itertools

## -----------------------------------------------

RETRY_COUNT = 4
ERROR_BIN = 5

rules = [
    Rule(lambda card: 'U' in card.color_identity, 1), # Blue cards to bin 1
    Rule(lambda card: 'R' in card.color_identity, 2), # Red cards to bin 2
    Rule(lambda card: 'W' in card.color_identity, 3), # White cards to bin 3
    Rule(lambda card: True, 4), # Everything else (i.e. black and green) to bin 4
    # Everything that the camera fails to read will go to the ERROR_BIN, which is 5
]

rules = rules_from_csv('user_input.csv')

## -----------------------------------------------

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_info(message):
    print(Colors.OKGREEN + message + Colors.ENDC)

def print_success(message):
    print(Colors.OKBLUE + message + Colors.ENDC)

def print_failure(message):
    print(Colors.FAIL + message + Colors.ENDC)

def print_warning(message):
    print(Colors.WARNING + message + Colors.ENDC)

## -----------------------------------------------

def rules_from_csv(file_name):
    rules = []
    with open('user_input.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            bin = row[0]
            colour = row[1]
            rules.append(Rule(lambda card: colour in card.color_identity, bin))
    return rules

## -----------------------------------------------

def candidate_names(raw_results):
    detected_strings = list(map(lambda str : re.sub(r'\W+', '', str), raw_results))
    permutations = list(itertools.permutations(detected_strings))
    return list(filter(lambda x: x != ' ', map(lambda x: ' '.join(x), permutations)))

def process_results(raw_results):
    #print("Raw: {}".format(raw_results))

    candidates = candidate_names(raw_results)
    #print("Candidates: {}".format(candidates))

    matched_card = Card.lookup(candidates)

    if matched_card == None:
        #print_failure("No match detected.\n")
        return None
    else:
        print_info("Matched: {} ({})".format(matched_card.name, ', '.join(matched_card.color_identity)))

    for rule in rules:
        if rule.predicate(matched_card):
            #print_success("Placing card in bin {}\n".format(rule.target_bin))
            return rule.target_bin
        else:
            continue

    return ERROR_BIN

## -----------------------------------------------

bin_controller = BinController()
bin_controller.connect()

retries = 0

for raw_results_up, raw_results_down in VideoTextRecognizer(source=0,threshold=1).decode_from_stream():
    #print("Raw up: {}".format(raw_results_up))
    #print("Raw down: {}".format(raw_results_down))

    bin_up = process_results(raw_results_up)
    bin_down = process_results(raw_results_down)

    if (bin_up == None and bin_down == None):
        print_failure("No match detected.\n")
        if retries >= RETRY_COUNT:
            print_warning("Retries exhausted. Placing card in error bin.\n")
            bin_controller.place_in_bin(ERROR_BIN)
            retries = 0
        else:
            retries += 1
    if bin_up != None and bin_down != None:
        print_failure("Matches detected in both up and down cases... wut?\n")
        if retries >= RETRY_COUNT:
            print_warning("Retries exhausted. Placing card in error bin.\n")
            bin_controller.place_in_bin(ERROR_BIN)
            retries = 0
        else:
            retries += 1
    if bin_up != None and bin_down == None:
        print_success("Card was right side up. Placing in bin {}.\n".format(bin_up))
        bin_controller.place_in_bin(bin_up)
        retries = 0
    if bin_up == None and bin_down != None:
        print_success("Card was upside down. Placing in bin {}.\n".format(bin_down))
        bin_controller.place_in_bin(bin_down)
        retries = 0

bin_controller.close()
print("[INFO] Closing.")
