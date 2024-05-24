import matplotlib.pyplot as plt
from data_processing import load_data, clean_data

def visualize_data(data):
    """Visualize the data."""
    data['column_name'].hist()
    plt.title('Histogram of Column Name')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    data = load_data('/Users/abdalrhmandarra/Desktop/data_visualization_project/data/data.csv')
    clean_data = clean_data(data)
    visualize_data(clean_data)
