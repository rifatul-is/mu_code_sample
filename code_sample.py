import os
import json

def load_data(file_path):
    """Loads data from a JSON file."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return {}

def save_data(file_path, data):
    """Saves data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def get_similar_terms(term, data):
    """Finds and returns terms similar to the given term from the dictionary."""
    term_lower_case = term.lower()
    return [key for key in data.keys() if term_lower_case in key.lower()]

def get_info(term, data):
    """Returns the information associated with the term, if it exists."""
    return data.get(term.lower(), None)

def add_or_update_term(term, description, data):
    """Adds or updates a term in the dictionary."""
    data[term.lower()] = description
    return f"Term '{term}' updated/added successfully."

def delete_term(term, data):
    """Deletes a term from the dictionary if it exists."""
    if term.lower() in data:
        del data[term.lower()]
        return f"Term '{term}' deleted successfully."
    else:
        return "Term not found."

def main():
    file_path = "data.json"
    data = load_data(file_path)
    end_loop = False

    print("Enter '0' to exit\n'1' for help\n'2' for adding or updating term\n'3' to delete term\n To search a term just enter it.")

    while not end_loop:
        term = input("Enter term : ")
        if term == "0":
            end_loop = True
        elif term == "1":
            print(list(data.keys()))
        elif term == "2":
            new_term = input("Enter the term to add/update: ")
            description = input("Enter the description: ")
            print(add_or_update_term(new_term, description, data))
            save_data(file_path, data)
        elif term == "3":
            del_term = input("Enter the term to delete: ")
            print(delete_term(del_term, data))
            save_data(file_path, data)
        else:
            info = get_info(term, data)
            if info:
                print(f"{term}: {info}")
            else:
                similar_terms = get_similar_terms(term, data)
                if not similar_terms:
                    print(f"No terms similar to '{term}'. Press '1' for Help.")
                else:
                    print("This term doesn't seem to exist. Here are some similar terms you can try:")
                    print(similar_terms)

main()
