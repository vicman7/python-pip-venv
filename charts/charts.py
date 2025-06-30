import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [30, 50, 80]

    fig, ax = plt.subplots() # Create a new figure and axis
    ax.pie(values, labels=labels) # Create a pie chart
    plt.savefig('pie.png') # Save the figure to a file
    plt.close()

