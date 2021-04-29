'''
Name: Kyle McLemore
Collaborator: Riley Zuckert
Date: 4/24/21
Class: ISTA 350 
'''
import pandas as pd, matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

def clean_data(csv_in):
    table = pd.read_csv(csv_in, usecols=['playlist_genre','valence','tempo'])
    rocktable = table[table['playlist_genre'] == 'rock']
    rockseries = pd.Series(data=rocktable['tempo'].values, index=rocktable['valence'].values)
    edmtable = table[table['playlist_genre'] == 'edm']
    edmseries = pd.Series(data=edmtable['tempo'].values, index=edmtable['valence'].values)
    return rockseries, edmseries

def make_plot(series,title,ylabel,xlabel):
    '''
    DO VALENCE (POSITIVITY) AND TEMPO HAVE A POSITIVE CORRELATION?
    '''
    series1, series2 = series
    fig, (top, bottom) = plt.subplots(2,sharex=True,sharey=True)
    fig.suptitle(title, fontsize=18)
    fig.tight_layout(pad=2.0)
    plt.subplots_adjust(hspace=0.1)
    for ax in fig.get_axes():
        ax.label_outer()
    #--------------------------------------------------------------------------------------
    x1 = series1.index.values
    y1 = series1.values
    top.plot(series1, linestyle='', marker='x', markersize=1, label='_nolegend_', color='#E51F79')

    m1, b1 = np.polyfit(x1, y1, 1)
    top.plot(x1, m1*x1 + b1, label='_nolegend_', color='#FFAE00')
    top.set_ylabel(ylabel, fontsize=15, labelpad=10)
    top_patch = mpatches.Patch(color='#E51F79', label='ROCK')
    top.legend(handles=[top_patch],loc=4)
    #--------------------------------------------------------------------------------------
    x2 = series2.index.values
    y2 = series2.values
    bottom.plot(series2, linestyle='', marker='x', markersize=1, label='_nolegend_', color='#9E3FF7')

    m2, b2 = np.polyfit(x2, y2, 1)
    bottom.plot(x2, m2*x2 + b2, label='_nolegend_', color='#FFAE00')
    bottom.set_xlabel(xlabel, fontsize=15, labelpad=5)
    bottom.set_ylabel(ylabel, fontsize=15, labelpad=10)
    bottom_patch = mpatches.Patch(color='#9E3FF7', label='EDM')
    bottom.legend(handles=[bottom_patch],loc=4)
    #--------------------------------------------------------------------------------------

def main():
    make_plot(clean_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv'),'TEMPO VS VALENCE','Tempo (BPM)','Valence Level')
    plt.show()

main()