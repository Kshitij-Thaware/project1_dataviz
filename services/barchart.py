import matplotlib.pyplot as plt

def display_barchart(column):

    column.value_counts().plot(kind='bar')
    plt.title('Bar Chart')