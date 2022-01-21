from modules.getdiscography import Artist
from modules.getinfo import Song
from modules.getsong import Lyrics
import argparse


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
group.add_argument('-f','--findsong', nargs="?", type=str,
 help='Input a short lyrics to find out songs which contain it')
args = parser.parse_args()
answer = args.song


if args.artist:
	response = input("Do you want to see the discography of the above-mentioned artist? (y/n) ->")
	if response == "y":
		print(Artist(args.artist, "resources/spotify_songs.csv").getdiscography())
	else:
		print("OK. If you want you can try with another artist!")

elif args.karaoke:
	response = input("Are you ready to start singing? (y/n) ->")
	if response == "y":
		print(Song(args.karaoke, "resources/spotify_songs.csv").karaoke())
	else:
		print("\nWe'll give you time to set up. Warm up your voice properly and try karaoke again!\n" +
			"And please, make sure to be ready for karaoke next time, you know...I got stuff to do!\n")

elif args.findsong:
	response = input("Do you want to find songs which contain this lyrics? (y/n) ->")
	if response == "y":
		print(Lyrics(args.findsong, "resources/spotify_songs.csv").getsong())

else:
	print(Song(args.song, "resources/spotify_songs.csv").getinfo())