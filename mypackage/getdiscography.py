#getdiscography

'''
The "getdiscography" function takes as input an artist name
and returns the whole discography of that artist present
in our database.
'''

def getdiscography(artist):
    songs = songs.lower() 
    db = pd.DataFrame(pd.read_csv('spotify_songs_final.csv'))
    tracks = list(db["track_name"])
    for i in range(len(tracks)):
        tracks[i] = tracks[i].lower()

    if songs in tracks:
        ind = tracks.index(songs)
        print(db["lyrics"][ind])
    else:
        print(songs + " seems not to be present in our database.") #WRONG INPUT CASE: recommendations of artists/songs
