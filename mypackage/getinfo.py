'''
The getinfo module contains the getinfo function which,
given a song title as input, returns information about
the artist, album, release date, genre and subgenre,
bpm, playback time and playlist.
'''

def getinfo(song):
    lyr = lyr.lower()
    db = pd.DataFrame(pd.read_csv('spotify_songs_final.csv'))
    all_lyr = list(db["lyrics"])
    for i in range(len(all_lyr)):
        all_lyr[i] = all_lyr[i].lower()
    n = 0
    
    for i in range(len(all_lyr)): #iterating through the each lyrics of the dataset
        for j in range(len(all_lyr[i-len(lyr)])): #accessing 
            if lyr == all_lyr[i][j:j+len(lyr)]:
                print(db["track_name"][i])
                n +=1
    if n == 0:
        print("So sorry! '" + lyr + "' seems not to be found in any song inside our database. Try with" +
              " something else") #WRONG INPUT CASE: Recommend different artists/songs
