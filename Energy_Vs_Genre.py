'''
Name: Kyle McLemore
Collaborator: Riley Zuckert
Date: 4/24/21
Class: ISTA 350 
'''
import pandas as pd, matplotlib.pyplot as plt
import numpy as np

def clean_data(csv_in):
    table = pd.read_csv(csv_in, usecols=['playlist_genre','energy'])
    series = pd.Series(data=table['energy'].values, index=table['playlist_genre'].values)
    genres = ['edm','latin','rock','r&b','rap','pop']
    avg_energy = []
    for item in genres:
        avg_energy.append(round(np.average(series[item].values),3))
    series = pd.Series(data=avg_energy,index=genres).sort_values()
    return series

def make_plot(series,title,ylabel,xlabel):
    '''
    DOES A SONGS LEVEL OF ENERGY INFLUENCE THE GENRE IT IS CONSIDERED TO BE?
    '''
    series.plot.bar(rot=0, zorder=3, color='#0EE580')
    plt.title(title, fontsize=18)
    plt.ylabel(ylabel, fontsize=15, labelpad=10)
    plt.xlabel(xlabel, fontsize=15, labelpad=5)
    plt.grid(which='major', axis='y', linestyle=':')

def main():
    make_plot(clean_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv'),'ENERGY VS GENRE','Energy Level','Genre')
    plt.show()

main()