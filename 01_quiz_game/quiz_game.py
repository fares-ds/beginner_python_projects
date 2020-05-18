import random


# Dictionary that contain the feature as key and his inventer as value
question_dict = {'Ballpoint pen': 'Biro Brothers', 'Jet Engine': 'Sir Frank Whittle',
                 'Gramophone': 'Thomas Alva Edison', 'Internal Combustion Engine': 'Otto',
                 'The Spinning Jeny': 'James Hargreaves', 'the small pox vaccine': 'Edward Jenner',
                 'Railway air brakes': 'George Westinghouse', 'Electric streetcar': 'Thomas Davenport',
                 'Electric Generator': 'Michal Faraday', 'Gun Powder': 'Roger Bacon'
                 }

mark = 0
# Turning the dict keys into a random list
question_list = list(question_dict.keys())
random.shuffle(question_list)
# loop through the random list of questions
for i, key in enumerate(question_list):
    print(40 * '-')
    print(f'{i + 1}- How invent {key}')

    # Give the user 4 choices, be sure that the choices are random and includes the right answer
    choices = list(question_dict.values())
    random.shuffle(choices)
    choices.remove(question_dict[key])
    choices = choices[:3]
    choices.append(question_dict[key])
    random.shuffle(choices)
    # Print the choices to the user
    for a, b in enumerate(choices):
        print(f"    {a + 1}- {b}")

    # Taking the user answer
    response = int(input('Enter your choice : '))

    # Evaluating the user answer
    if choices[response - 1] == question_dict[key]:
        mark += 1.0
    else:
        mark -= 0.5

    print(question_dict[key])
print('-------------------------')
print(f"You have got {mark}/10")
