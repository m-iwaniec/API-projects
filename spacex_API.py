import requests


info = requests.get('https://api.spacexdata.com/v4/company')
print(info.text)
print('\n')

info_json = info.json()
print("Information about SpaceX", info_json['headquarters'])
print("\n")

print("SpaceX address: " + info_json['headquarters']['address'] + ", " + info_json['headquarters']['state'] + ", " +
      info_json['headquarters']['city'])
print("SpaceX info: " + "founder: " + info_json['founder'] + ", founded: " + str(info_json['founded']) + ", employees: "
      + str(info_json['employees']) + ", CEO: " + info_json['ceo'] + ", summary: " + info_json['summary'])


print("----------------------------------------------------------")


capsules = requests.get('https://api.spacexdata.com/v4/capsules')
print(capsules.text)
print('\n')
capsules_json = capsules.json()

n = 1
for i in capsules_json[0:10]:
    print(n, "Type of capsule: ", i['type'], "\n", "Status: ", i['status'], "\n", "Reuse count: ", i['reuse_count'], "\n", "Water landings: ", i['water_landings'], "\n", "Land landings: ", i['land_landings'])
    n = n + 1

# print("Reuse count: ", capsules_json[0]['reuse_count'])
# print("Water landings: ", capsules_json[1]['water_landings'])
# print("Land landings: ", capsules_json[2]['land_landings'])
# print("Type of capsule: ", capsules_json[7]['type'])
# print("Status: ", capsules_json[6]['status'])

print("--------------------------------------------------------------")

events = requests.get('https://api.spacexdata.com/v4/history/')
print(events.text)
print('\n')
events_json = events.json()

n = 1
for i in events_json[0:10]:
    print(n, i['title'], "\n", i['event_date_utc'], "\n", i['details'], "\n", i['links']['article'])
    n = n + 1

print("--------------------------------------------------------------")

crew = requests.get('https://api.spacexdata.com/v4/crew')
print(crew.text)
print('\n')
crew_json = crew.json()

n = 1
for i in crew_json[0:10]:
    print(n, i['name'], "\n", i['agency'], "\n", i['image'], "\n", i['wikipedia'], "\n", i['status'])
    n = n + 1

print("--------------------------------------------------------------")

ships = requests.get('https://api.spacexdata.com/v4/ships')
print(ships.text)

print('\n')
ships_json = ships.json()

n = 1
for i in ships_json[0:10]:
    comma = ', '.join(i['roles'])
    print(n, "Name:", i['name'], "\n", "Type:", i['type'], "\n", "Role:", comma, "\n", "Built in:", i['year_built'], "\n", i['image'])
    n = n + 1
