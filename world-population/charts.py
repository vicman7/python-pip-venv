import matplotlib.pyplot as plt
import matplotlib

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    #plt.show()
    plt.savefig(f'./imgs/{name}.png') # Save the figure to a file
    plt.close()

def generate_pie_chart(name, labels, sizes):
    colors = plt.cm.Paired.colors[:len(labels)]

    plt.figure(figsize=(10,6))
    plt.pie(sizes, labels = labels, autopct='%1.1f%%', colors=colors, startangle=0, wedgeprops={'edgecolor': 'black'})
    plt.title('World population by country')
    plt.axis('equal')
    #plt.show()
    plt.savefig(f'./imgs/{name}.png') # Save the figure to a file
    plt.close()

if __name__ == '__main__':
    generate_bar_chart()
