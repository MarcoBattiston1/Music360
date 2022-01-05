'''
The Artist class contains the getdiscography function which,
given an artist name as input, returns the whole set of songs
by that artist which are contained in our dataset.
If the input is not present in our dataset, the function
returns some suggestions about valid input
'''

class Artist:
    def __init__(self, artist_name):
        self.artist_name = artist_name

    @staticmethod
    def getdiscography(artist_name):
        import pandas as pd
        artist_name = artist_name.lower().strip()
        db = pd.read_csv('mypackage/spotify_songs.csv')
        discography = []
        for i in range(len(db.track_artist)):
            if artist_name == db.track_artist[i].lower():
                discography.append(db.track_name[i])
        if len(discography) ==0:
            return("The artist you're looking for is not present in our database. "+
                  "Here you are some recommended artist we have:\n" + 
                  "'Mariah Carey',\n" +
                  "'Madison Beer',\n" +
                  "'GASHI'!")
        print(artist_name.title(), "made the following songs:")
        print(*discography, sep="\n")
