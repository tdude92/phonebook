import json

name = input("Full Name: ")
city = input("City: ")
phone = int("".join(list(filter(lambda x: x not in (" ", "-", "(", ")"), input("Phone Number: ")))))

entry = {"name": name, "city": city, "phone": phone}

with open("entries.json", "r") as read_file:
    data = json.loads(read_file.read())

data[len(data) + 1] = entry

with open("entries.json", "w") as write_file:
    json.dump(data, write_file, indent=4)
