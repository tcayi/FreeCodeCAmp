import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = np.arange(df['Year'].min(),2050,1)
    y_pred = x_pred*res.slope + res.intercept

    plt.plot(x_pred,y_pred)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]

    res2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred2 = np.arange(2000,2050,1)
    y_pred2 = x_pred2*res2.slope + res2.intercept

    plt.plot(x_pred2,y_pred2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()