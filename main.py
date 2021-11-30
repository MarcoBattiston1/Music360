from mypackage/getdiscography import Artist
from mypackage/getinfo import Song
import argparse
import pandas as pd


db = pd.DataFrame(pd.read_csv('mypackage/spotify_songs.csv'))
parser = argparse.ArgumentParser(description='This program will' +
                                             ' give you information' +
                                             ' about the song you input' +
                                             ' if it is present in our database.')

