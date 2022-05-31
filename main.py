import json
jsonFile = "num.json"
x = json.load(open(jsonFile))['x']
while True:
    print(f"x:{x}")
    n = x
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (n * 3) + 1
        #print(f"n:{n}")
    x += 1
    json_data = json.load(open(jsonFile, 'r'))
    json_data['x'] = x
    json.dump(json_data, open(jsonFile, 'w'))
    #print()
