import csv
import config
# from datetime import datetime

opFolder = config.output_path
# now = str(datetime.now())


# csvFileName = f'{opFolder}{now}.csv'

csvFileName = f'{opFolder}test.csv'




def makeCSV(payload):
    # Check if the CSV file exists, if not, write header
    try:
        with open(csvFileName, 'x', newline='',encoding='utf-8') as csvfile:
            fieldnames = payload.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(payload)
    except FileExistsError:
        pass

    # Write the payload to the CSV file
    with open(csvFileName, 'a', newline='',encoding='utf-8') as csvfile:
        fieldnames = payload.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(payload)