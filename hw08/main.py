#Задание 1
import requests
import json


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

#Задание 2
# import requests

def upload_to_yandex_disk(path, token, filename):
    URL = "https://cloud-api.yandex.net/v1/disk/resources/upload?path="+filename

    headers = {
        "Accept": "application/json",
        "Authorization": f"OAuth {token}",
    }
    upload_URL = (requests.get(URL, headers=headers)).json()["href"]
    with open(path, "rb") as f:
        files = {"file": (filename, f)}
        response = requests.put(upload_URL, headers=headers, files=files)

    if response.status_code == 201:
        return response.json()["href"]
    else:
        raise Exception("Failed to upload file")

upload_to_yandex_disk("C:\\16700566174011.mp4", "", "16700566174011")