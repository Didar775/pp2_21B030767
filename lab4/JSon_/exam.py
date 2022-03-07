import json

with open('my.json', 'r') as file:
    data = json.load(file)

print('Interface Status')
print(80*'=')
print('DN', 47*' ', 'Description', 10*' ', 'Speed', '  ', 'MTU')
print(50*'-', 20*'-', ' ', 6*'-', ' ', 6*'-')

dict = data["imdata"][0]["l1PhysIf"]['attributes'].copy()
for i in range(3):
    dict = data["imdata"][i]["l1PhysIf"]['attributes'].copy()

    print(dict['dn'], 29*' ', dict['speed'], 2*' ', dict['mtu'])
