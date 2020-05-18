# make a list to hold onto our new_items
shopping_list = []


# show the list items
def show_items(lst):
    print("Here is your list: ")
    for item in lst:
        print(f"--> {item}")


# show a helping list
def show_help():
    # print out instructions on how to use the app
    print("What should we pick up at the store?")
    print('''
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
    ''')


def add_items(item):
    # add new new_items to our List
    shopping_list.append(item)
    print(f"Added {item}. List now has {len(shopping_list)} items.")


show_help()

while True:
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break

    elif new_item == 'SHOW':
        show_items(shopping_list)
        continue

    elif new_item == 'HELP':
        show_help()
        continue

    add_items(new_item)
