import csv

def process_csv(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        array = []
        for line in csv_reader:
            array = line

        print(array)
        # return array