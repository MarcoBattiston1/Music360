"""
The Song class contains the getinfo function which,
given a song title as input, returns information about
the artist, album, release date, playlist in which it
appeared, genre and subgenre of the playlist,
bpm of the song and playback time.
"""


# importing needed libraries
import pandas as pd
import os


# creating a class named Song
class Song:

    def __init__(self, song_name, path):  # initializing object
        self.song_name = song_name
        self.path = path

    # defining the function to return song info
    def getinfo(self):
        song_name = self.song_name.lower().strip()
        # assigning the database to the variable "db"
        db = pd.read_csv(self.path)
        # creating a list with all song titles
        titles = list(db["track_name"].str.lower())

        if song_name in titles:
            # assinging the index number to variable i
            i = titles.index(song_name)
            # returning info
            return ("\nThe song: '" + db.track_name[i] + "' is made by '" +
                    db.track_artist[i] + "'.\nIt was released in the album '" +
                    db.track_album_name[i] + "', in the date " +
                    db.track_album_release_date[i] + ", and it appeared" +
                    " in the spotify playlist named " +
                    db.playlist_name[i] + ", with other song of genre " +
                    db.playlist_genre[i] + ", and subgenre " +
                    db.playlist_subgenre[i] + ".\nThe song has " +
                    str(round(db.tempo[i])) + " bpm and it lasts " +
                    str(round(db.duration_ms[i] / 1000)) + " seconds.\n")
        else:
            return (" The song you're looking for" +
                    " is not present in our database. " +
                    " Here you are some recommended songs we have:\n " +
                    " 'Party Rock Anthem',\n " +
                    " 'Symphony Of Destruction',\n " +
                    " 'Some Nights'! ")

    # defining the function to create a karaoke
    def karaoke(self):
        song_name = self.song_name.lower().strip()
        db = pd.read_csv(self.path)
        # creating a list with all song titles
        titles = list(db["track_name"].str.lower())

        if song_name in titles:
            # assinging the index number to variable i
            i = titles.index(song_name)
            # returning song URL and song lyrics
            return (" \nType this in your favourite browser: 'spotify:track:" +
                    str(db.track_id[i]) + "' and sing with our lyrics!\n\n " +
                    db.track_name[i].upper() +
                    " - " + db.track_artist[i].upper() +
                    "\n\n" +
                    str(db.lyrics[i]))
        else:
            # returning recommendations, if song not present
            return ("Not found!\nHere you are" +
                    " some recommended songs we have:\n" +
                    "'Party Rock Anthem',\n" +
                    "'Symphony Of Destruction',\n" +
                    "'Some Nights'!")
