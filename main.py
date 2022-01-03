from mypackage.getdiscography import Artist
from mypackage.getinfo import Song
import argparse
#import pandas as pd



#db = pd.DataFrame(pd.read_csv('mypackage/spotify_songs.csv'))
parser = argparse.ArgumentParser(description='This program will' +
                                             ' give you information' +
                                             ' about the song you input' +
                                             ' if it is present in our database.')


group = parser.add_mutually_exclusive_group()
parser.add_argument('song', type=str, nargs="?", help='Input the song title you want to have info about')
group.add_argument('-a','--artist', nargs="?", type=str,
 help='Input the artist name to get his discography')
group.add_argument('-k','--karaoke', nargs="?", type=str,
 help='Input a song title to start karaoke')
args = parser.parse_args()
answer = args.song

# if __name__=='__main__':
# 	print(Song.getinfo(args.song))

#if __name__ == "__main__":
#    Song.getinfo("Party Rock Anthem")

if args.artist:
	response = input("Do you want to see the discography of the above-mentioned artist? (y/n) ->")
	if response == "y":
		Artist.getdiscography(args.artist)
	else:
		print("OK. If you want you can try with another artist!")

elif args.karaoke:
	response = input("Are you ready to start singing? (y/n) ->")
	if response == "y":
		Song.karaoke(args.karaoke)
	else:
		print("We'll give you time to set up. Warm up your voice properly and try karaoke again!")

else:
	Song.getinfo(args.song)
	response = input("Do you want to make a karaoke of this song? (y/n) ->")
	if response == "y":
		Song.karaoke(args.song)





