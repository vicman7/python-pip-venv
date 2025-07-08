import csv
import matplotlib.pyplot as plt

# mi solución: no usé otros módulos
def world_population(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        header = next(reader)
        country = header.index('CCA3')
        wpp = header.index('World Population Percentage')
        country_dict = {row[country]: float(row[wpp]) for row in reader}

    sorted_countries = sorted(country_dict.items(), key = lambda x: x[1], reverse=True)
    top_10 = sorted_countries[:10]
    others = sum(value for _, value in sorted_countries[10:]) #_ throwaway variable in Python meaning that we don't need country name so we in¿gnore them using _
    top_10.append(('Others', others))

    labels, sizes = zip(*top_10) #*top_10, it unpacks the list of tuples so that zip() gets separate sequences
    
    colors = plt.cm.Paired.colors[:len(labels)]

    plt.figure(figsize=(10,6))
    plt.pie(sizes, labels = labels, autopct='%1.1f%%', colors=colors, startangle=0, wedgeprops={'edgecolor': 'black'})
    plt.title('World population by country')
    plt.axis('equal')

if __name__ =='__main__':
    world_pop_per = world_population('./world_population.csv')
    plt.show()