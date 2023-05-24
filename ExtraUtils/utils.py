import csv
import os.path

def read_state(path: os.path):
    """
        this function read a csv file that contain iran states
        and return it in a dict format
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    data = []

    with open(file=path, mode="r", encoding="UTF-8") as fp:
        RowReader = csv.DictReader(fp)
        for row in RowReader:
            keys = row.keys()

            temp = {}
            for key in keys:
                temp[key] = row[key]

            data.append(temp)

        return data

