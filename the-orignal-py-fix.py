json_data = []
with open('the json file path after the download.json')as fp:
    for i in fp:
        json_data.append(json.loads(i))
data = []

for i in json_data:
    data.append(i['Text'])