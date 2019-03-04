import json

def add_entry(name, city, phone):
    entry = {"name": name, "city": city, "phone": phone}

    with open("entries.json", "r") as read_file:
        data = json.loads(read_file.read())

    data.append(entry)

    with open("entries.json", "w") as write_file:
        json.dump(data, write_file, indent=4)


def del_entry(name, city, phone):
    with open("entries.json", "r") as read_file:
        data = json.loads(read_file.read())

    for i in range(len(data)):
        if data[i] == {"name": name, "city": city, "phone": phone}:
            data.pop(i)
            break
    
    with open("entries.json", "w") as write_file:
        json.dump(data, write_file, indent = 4)


if __name__ == "__main__":
    name = input("Full Name: ")
    city = input("City: ")
    phone = int("".join(list(filter(lambda x: x not in (" ", "-", "(", ")"), input("Phone Number: ")))))

    while True:
        try:
            action = int(input("Would you like to...\n  1. Add Entry\n  2. Delete Entry\n"))
            if action > 2 or action < 1:
                raise ValueError
        except ValueError:
            print("Please input a valid integer!")
        else:
            break

    if action == 1:
        add_entry(name, city, phone)
    else:
        del_entry(name, city, phone)
