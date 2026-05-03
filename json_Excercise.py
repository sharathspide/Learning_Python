import json

with open("data.json", "r") as file:
    context = file.read()
    print (context)

data = {
    "name": "SHARATH RA",
    "age": 27,
    "emp_id": "2892553_tcs"
}

with open("data.json", "a") as file:
    json.dump(data, file)
