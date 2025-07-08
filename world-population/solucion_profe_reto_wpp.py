import read_csv
import charts

def run(path):
    data = read_csv.read_csv(path)
    #data = list(filter(lambda country: country['Continent'] == 'South America', data))
    countries = list(map(lambda x:x['CCA3'], data))
    percentages = list(map(lambda x:float(x['World Population Percentage']), data))
    sorted_data = sorted(zip(percentages, countries), reverse=True)
    top10 = sorted_data[:10]
    others = sum(value for value, _ in sorted_data[10:])
    top10.append((others, 'Others'))
    sorted_percentages, sorted_countries = zip(*top10)
    sorted_percentages = list(sorted_percentages)
    sorted_countries = list(sorted_countries)
    print(sorted_percentages)
    print(sorted_countries)
    file_name = 'international'
    charts.generate_pie_chart(file_name, sorted_countries, sorted_percentages)

if __name__ =='__main__':
    data = run('./world_population.csv')