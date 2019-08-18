import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def close_matches(w):
    list_of_matches = get_close_matches(w, data.keys(), 20, 0.7)
    return list_of_matches


def define(w):
    w = w.lower()
    list_matches = close_matches(w)

    if w in data:
        return data[w]

    elif w.capitalize() in data:
        return data[w.capitalize()]

    elif w.upper() in data:
        return data[w.upper()]

    elif len(list_matches) > 0:
        message = f"Please enter a valid word, if the word you meant is this enter 'Y', otherwise enter 'N'"
        print('=' * len(message))
        print(list_matches)
        yn = input(message)
        print('=' * len(message))

        if yn.capitalize() == "Y":
            user_input = input('Enter the word from the list : ')
            return define(user_input)

        elif yn.capitalize() == "N":
            return "The word doesn't exist. Please double check it."

        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."


sentence = "Enter word: "
print('=' * len(sentence))
word = input(sentence)
output = define(word)
if type(output) == list:
    for item in output:
        print('=' * len(item))
        print(item)
else:
    print('=' * len(output))
    print(output)