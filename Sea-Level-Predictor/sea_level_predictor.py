import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, y)

    # Create first line of best fit
    line1 = linregress(x, y)
    x_pred1 = pd.Series([i for i in range(1880,2051)])
    y_pred1 = line1.slope * x_pred1 + line1.intercept
    plt.plot(x_pred1, y_pred1, 'r')

    # Create second line of best fit
    newdf = df.loc[df["Year"] >= 2000]
    x_new = newdf['Year']
    y_new = newdf['CSIRO Adjusted Sea Level']
    line2 = linregress(x_new, y_new)
    x_pred2 = pd.Series([i for i in range(2000,2051)])
    y_pred2 = line2.slope * x_pred2 + line2.intercept
    plt.plot(x_pred2, y_pred2, 'b')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()