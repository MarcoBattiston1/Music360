from mypackage.getdiscography import Artist
from mypackage.getinfo import Song
from mypackage.getsong import Lyrics
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
		Artist.getdiscography(args.artist)
	else:
		print("OK. If you want you can try with another artist!")

elif args.karaoke:
	response = input("Are you ready to start singing? (y/n) ->")
	if response == "y":
		Song.karaoke(args.karaoke)
	else:
		print("We'll give you time to set up. Warm up your voice properly and try karaoke again!")

elif args.findsong:
	response = input("Do you want to find songs which contain this lyrics? (y/n) ->")
	if response == "y":
		Lyrics.getsong(args.findsong)

else:
	Song.getinfo(args.song)
	response = input("Do you want to make a karaoke of this song? (y/n) ->")
	if response == "y":
		Song.karaoke(args.song)





