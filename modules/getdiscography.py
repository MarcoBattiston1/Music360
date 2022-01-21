'''
The Artist class contains the getdiscography function which,
given an artist name as input, returns the whole set of songs
by that artist which are contained in our dataset.
If the input is not present in our dataset, the function
returns some suggestions about valid input
'''


#importing needed libraries
import pandas as pd
import sys
from sys import path


#creating a class named Artist
class Artist:

    def __init__(self, artist_name, db_path):   #initializing the object's attributes
        self.artist_name = artist_name
        self.db_path = db_path


    def getdiscography(self):   #defining the function to return artist discography
        artist_name = self.artist_name.lower().strip()
        db = pd.read_csv(self.db_path)    #assigning the database to the variable "db"
        discography = []

        for i in range(len(db.track_artist)):   #iterating through all the artists
            if artist_name == db.track_artist[i].lower():
                discography.append(db.track_name[i])    #appending all artist songs to a list
        
        if len(discography) ==0:    #if no songs found, return recommendations
            return(" The artist you're looking for is not present in our database. "+
                  " Here you are some recommended artist we have:\n " + 
                  " 'Mariah Carey',\n " +
                  " 'Madison Beer',\n " +
                  " 'GASHI'! ")
        
        return ("\n" + artist_name.title() + " " +
          "made the following songs:\n\n" + "\n".join(discography))
