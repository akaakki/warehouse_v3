from data import personnel



def flatten_list(personnel):
    persons = []
    for person in personnel:
        persons.append(person)
        if "head_of" in person:
            flatten_list(person['head_of'])
            del person['head_of']
    return persons


def log_user_in(user_name):
    if user_name is None:
        user_name = input("Reenter username: ")
        
    persons = flatten_list(personnel)
    user_password = input("Password: ")

    for user_data in persons:
        if user_name == user_data['user_name'] and user_password == user_data['password']:
            return True
    return False
