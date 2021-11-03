import requests


# Current ISS Location
where = requests.get('http://api.open-notify.org/iss-now.json')
print(where.text)

where_json = where.json()
print(where_json)
print("\n")

# To print the number of people in space
print("Position of ISS in space:", where_json['iss_position'])
print("\n")


# People in space
people = requests.get('http://api.open-notify.org/astros.json')
print(people.text)

people_json = people.json()
print(people_json)
print("\n")

# To print the number of people in space
print("Number of people in space:", people_json['number'])
print("\n")


# To print the names of people in space using a for loop
n = 1
for p in people_json['people']:
    print(n, p['name'])
    n = n + 1

