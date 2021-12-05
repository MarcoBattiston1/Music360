from mypackage/getdiscography import Artist
from mypackage/getinfo import Song
import argparse
import pandas as pd



db = pd.DataFrame(pd.read_csv('mypackage/spotify_songs.csv'))
parser = argparse.ArgumentParser(description='This program will' +
                                             ' give you information' +
                                             ' about the song you input' +
                                             ' if it is present in our database.')


group = parser.add_mutually_exclusive_group()
parser.add_argument('song', type=str, help='Input the song title you want to have info about')
group.add_argument('-a','--artist', type=str, action="store_true",
 help='Input the artist name to get his discography')
group.add_argument('-k','--karaoke', type=str, action="store_true",
 help='Input a song title to start karaoke')
args = parser.parse_args()
answer = args.song

if __name__=='__main__':
	print(Song.getinfo(args.song))


