import requests
import json

# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
# print(todos)

all_heroes = requests.get("https://akabab.github.io/superhero-api/api/all.json")
all_heroes_json = json.loads(all_heroes.text)

heroes_list = ['Hulk', 'Captain America', 'Thanos']
intelligence_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}

for i in heroes_list:
    for j in all_heroes_json:
        if i == j["name"]:
            intelligence_dict[i] = j["powerstats"]["intelligence"]

intelligence_dict = dict([max(intelligence_dict.items())])
print(f"Самым умным является:{list(intelligence_dict.keys())[0]}")
