import json
import csv
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    with open("input.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"')
        json_data = list(reader)
    with open("output.json", "w") as f:
        json.dump(json_data, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
