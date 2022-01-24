'''
The Artist class contains the getdiscography function which,
given an artist name as input, returns the whole set of songs
by that artist which are contained in our dataset.
If the input is not present in our dataset, the function
returns some suggestions about valid input
'''


# importing needed libraries
import pandas as pd
import sys
from sys import path


# creating a class named Artist
class Artist:
    # initializing the object's attributes
    def __init__(self, artist_name, db_path):
        self.artist_name = artist_name
        self.db_path = db_path

    # defining the function to return artist discography
    def getdiscography(self):

        artist_name = self.artist_name

        #handling none input type
        if type(self.artist_name) is type(None):
            return("None input type not accepted." + 
                   "\nPlease provide a string input.")

        artist_name = self.artist_name.lower().strip()
        # assigning the database to the variable "db"
        db = pd.read_csv(self.db_path)
        discography = []
        # iterating through all the artists
        for i in range(len(db.track_artist)):
            if artist_name == db.track_artist[i].lower():
                # appending all artist songs to a list
                discography.append(db.track_name[i])
        # if no songs found, return recommendations
        if len(discography) == 0:
            return("The artist you're looking for" +
                   " is not present in our database. " +
                   "Here you are some recommended artist we have:\n " +
                   "'Mariah Carey',\n " +
                   "'Madison Beer',\n " +
                   "'GASHI'! ")

        return ("\n" + artist_name.title() + " " +
                "made the following songs:\n\n" +
                "\n".join(discography))
