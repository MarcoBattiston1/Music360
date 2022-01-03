'''
The Song class contains the getinfo function which,
given a song title as input, returns information about
the artist, album, release date, playlist in which it
appeared, genre and subgenre of the playlist,
bpm of the song and playback time.
'''

class Song:
    def __init__(self, song_name):
        self.song_name = song_name

    @staticmethod
    def getinfo(song_name):
        import pandas as pd
        song_name = song_name.lower().strip()
        db = pd.DataFrame(pd.read_csv('mypackage/spotify_songs.csv'))
        counter = 0
        for i in range(len(db.track_name)):
            if song_name == db.track_name[i].lower():
                print("\nThe song: '", db.track_name[i],"' is made by '",
                     db.track_artist[i], "'.\nIt was released in the album '",
                      db.track_album_name[i], "', in the date ", 
                      db.track_album_release_date[i], ", and it appeared in the spotify playlist named: '",
                      db.playlist_name[i], "', with other song of genre ",
                     db.playlist_genre[i], ", and subgenre ",
                     db.playlist_subgenre[i],".\nThe song has ",
                     round(db.tempo[i])," bpm and it lasts ",
                     round(db.duration_ms[i]/1000)," seconds.\n", sep="")
                counter += 1
                break
        if counter ==0:
            print("\nThe song you're looking for is not present in our database. "+
                  "Here you are some recommended songs we have:\n" + 
                  "'Party Rock Anthem',\n" +
                  "'Symphony Of Destruction',\n" +
                  "'Some Nights'!\n")

    @staticmethod
    def karaoke(song_name):
        import pandas as pd
        song_name = song_name.lower().strip()
        db = pd.DataFrame(pd.read_csv('mypackage/spotify_songs.csv'))
        counter = 0
        for i in range(len(db.track_name)):
            if song_name == db.track_name[i].lower():
                print("\nType this in your favourite browser: 'spotify:track:",
                             str(db.track_id[i]), "' and sing with our lyrics!\n\n",
                             db.track_name[i].upper(), " - ", db.track_artist[i].upper(), "\n\n",
                            str(db.lyrics[i]), "\n" ,sep="")
                counter += 1
                break
        if counter == 0:
            print("Not found!\nHere you are some recommended songs we have:\n" + 
                  "'Party Rock Anthem',\n" +
                  "'Symphony Of Destruction',\n" +
                  "'Some Nights'!")

