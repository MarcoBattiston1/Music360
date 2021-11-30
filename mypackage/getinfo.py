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

    def getinfo(song_name):
        import pandas as pd
        song_name = song_name.lower().strip()
        db = pd.DataFrame(pd.read_csv('spotify_songs.csv'))
        counter = 0
        for i in range(len(db.track_name)):
            if song_name == db.track_name[i].lower():
                return(print("The song: '", db.track_name[i],"' is made by '",
                     db.track_artist[i], "'. It was released in the album '",
                      db.track_album_name[i], "', in the date", 
                      db.track_album_release_date[i], ", and it appeared in the spotify playlist named",
                      db.playlist_name[i], ", with other song of genre",
                     db.playlist_genre[i], ", and subgenre",
                     db.playlist_subgenre[i],". The song has",
                     round(db.tempo[i]),"bpm and it lasts",
                     round(db.duration_ms[i]/1000),"seconds."))
                counter += 1
                break
        if counter ==0:
            return(print("The song you're looking for is not present in our database. "+
                  "Here you are some recommended songs we have:\n" + 
                  "'Party Rock Anthem',\n" +
                  "'Symphony Of Destruction',\n" +
                  "'Some Nights'!"))

