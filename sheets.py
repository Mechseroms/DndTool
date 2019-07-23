import csv


def load_sheet(path_to_csv):
    try:
        with open(path_to_csv, 'r') as file:
            sheet = [row for row in csv.reader(file)][1:]
    except FileNotFoundError:
        print(f"{path_to_csv} does not exist")
        sheet = []

    return sheet

