import csv
import re
import matplotlib.pyplot as plt

def country_chart(path, country):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        #data = []
        for row in reader:
            iterable = zip(header,row)
            country_dict = {key: value for (key, value) in iterable}
            
            if country_dict['Country/Territory'] == country:
                pattern = r'^(\d{4}) '
                data = {re.match(pattern, key).group(1): value for key, value in country_dict.items() if re.match(pattern, key)} #.group(1) extracts the captured year from the matched pattern.
        #return data
        years = sorted(map(int, data.keys()))
        values = [data[str(year)] for year in years]

        plt.figure()
        plt.plot(years, values, marker = 'o', linestyle = '-', color = 'purple')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title(country)
        return plt
    
if __name__ =='__main__':
    user_preference = input('Enter a country name: ')
    if not user_preference:
        user_preference = 'Colombia'
    country = country_chart('./world_population.csv', user_preference)
    plt.savefig(f'./imgs/{user_preference}.png')