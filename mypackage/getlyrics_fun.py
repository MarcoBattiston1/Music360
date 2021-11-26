#getlyrics_fun

def lyrics1(songs):
    songs = songs.lower() 
    db = pd.DataFrame(pd.read_csv('spotify_songs_final.csv'))
    tracks = list(db["track_name"])
    for i in range(len(tracks)):
        tracks[i] = tracks[i].lower()

    if songs in tracks:
        ind = tracks.index(songs)
        print(db["lyrics"][ind])
    else:
        print(songs + " seems not to be present in our database.")
