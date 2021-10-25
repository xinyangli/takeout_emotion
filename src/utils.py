import csv
def ReadCSV(file):
    """
    Read data from csv file to memory
    """
    try:
        with open(file, newline='') as csvfile:
            datareader = csv.reader(csvfile)
            data = [x for x in datareader]
            csvfile.close()
        return data
    except FileNotFoundError as e:
        print(e)
        return []

def WriteCSV(file, dataset):
    with open(file, "w", newline='') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerows(dataset)
        csvfile.close()