import csv
import json


def main():
    csvfile = open('data/images.csv', 'r')
    jsonfile = open('data/images.json', 'w')

    fieldnames = ('filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax', 'image_id')
    reader = csv.DictReader(csvfile, fieldnames)
    jsonfile.write('[')
    id_value = 0
    for row in reader:
        row['id'] = '{}'.format(id_value)
        id_value += 1
        json.dump(row, jsonfile, indent=4)
        jsonfile.write(',')
        jsonfile.write('\n')
    jsonfile.write(']')
    print('Successfully converted csv to json.')


main()
