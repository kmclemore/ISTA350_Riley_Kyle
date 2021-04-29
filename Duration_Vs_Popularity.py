'''
Name: Kyle McLemore
Collaborator: Riley Zuckert
Date: 4/24/21
Class: ISTA 350 
'''
import pandas as pd, matplotlib.pyplot as plt
import numpy as np

def clean_data(csv_in):
    table = pd.read_csv(csv_in, usecols=['duration_ms','track_popularity'])
    series = pd.Series(data=table['track_popularity'].values, index=table['duration_ms'].values/60000)
    return series

def make_plot(series,title,ylabel,xlabel):
    '''
    DOES SONG DURATION HAVE AN EFFECT ON SONG POPULARITY?
    '''
    x = series.index.values
    y = series.values
    series.plot(linestyle='', marker='x', markersize=.5, label='_nolegend_')

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, label='Linear Reg')

    quad = np.poly1d(np.polyfit(x, y, 2))
    xx = np.linspace(0, 10, 100)
    plt.plot(xx, quad(xx),label='Quadratic Reg')

    cubic = np.poly1d(np.polyfit(x, y, 3))
    xx = np.linspace(0, 10, 100)
    plt.plot(xx, cubic(xx),label='Cubic Reg')

    #print(polyfit(x, y, 1))     #2.06% of the variation in the reported popularity levels can be explained by the song duration.
    #print(polyfit(x, y, 2))     #2.22% of the variation in the reported popularity levels can be explained by the song duration.
    #print(polyfit(x, y, 3))     #2.70% of the variation in the reported popularity levels can be explained by the song duration.

    plt.title(title, fontsize=18)
    plt.ylabel(ylabel, fontsize=15)
    plt.xlabel(xlabel, fontsize=15)
    plt.legend()

def polyfit(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    #calculate r-squared
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['r_squared'] = ssreg / sstot

    return results

def main():
    make_plot(clean_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv'),'SONG DURATION VS POPULARITY','Popularity Score','Song Duration (Mins)')
    plt.show()

main()