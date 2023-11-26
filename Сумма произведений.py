import json
FILENAME = "input.json"
def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    sum_ = sum([item["score"]*item["weight"] for item in json_data])
    return round(sum_, 3)


print(task())
