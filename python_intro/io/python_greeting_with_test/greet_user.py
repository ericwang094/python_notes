import json


def get_stored_username():
    filename = 'username.json'

    username = None
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None

    return username


def get_new_username():
    username = input("what's your name \n")
    filename = 'username.json'
    with open(filename, 'w') as f_object:
        json.dump(username, f_object)
    return username


def greet_user():
    username = get_stored_username()
    if username is None:
        get_new_username()
        print(f'we will remember you next time when you back {username}')
    else:
        print(f"welcome back {username}")

greet_user()
