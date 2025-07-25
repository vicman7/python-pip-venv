import csv
import matplotlib.pyplot as plt

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') # iterable
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row) #tuples array
            #print(list(iterable))
            country_dict = {key: value for (key,value) in iterable}
            data.append(country_dict)
        return data


if __name__ =='__main__':
    data = read_csv('./world_population.csv')

    print(data[0])