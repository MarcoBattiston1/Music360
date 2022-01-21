'''
This module contains a function named get_song,
which takes as input a string given by the user
and check if that string is present in any lyrics
present in the dataset, through an iteration.
The function returns all the matches find,
but stops at 50 songs in order to keep the output clear.
'''

#importing needed libraries
import pandas as pd




#creating a class named Lyrics
class Lyrics:

    def __init__(self, lyr, path):      #initializing the object's attributes
        self.lyr = lyr
        self.path = path


    def getsong(self):                  #defining the function to return the song in which the text is found
        lyr = str(self.lyr)
        lyr = self.lyr.lower()          #lowering user string input

        #handling wrong input
        wrong_input = ["", " "]
        if str(lyr) in wrong_input:
            return "Empty input is not supported by the program. Try with something different!"

        db = pd.read_csv(self.path)
        all_lyr = list(db["lyrics"])    #creating a list with all lyrics of all songs
        for i in range(len(all_lyr)):
            all_lyr[i] = all_lyr[i].lower()     #lowering all lyrics of the list
        n = 0

        if "mypackage" in self.path:
            print("This could take a while...\n")
        res = ""

        for i in range(len(all_lyr)):  #iterating through each lyrics of the dataset
            for j in range(len(all_lyr[i]) - len(lyr)+1):  #accessing each set of words of len(lyr)
                if lyr == all_lyr[i][j:j + len(lyr)]:      #comparing user input & lyrics
                    res += db["track_name"][i].upper() + " - " + db["track_artist"][i].upper() + "\n"
                    n += 1
                    if n >= 50:                            #setting execution stopper at 50th result
                        return (res + "\nExecution stopped at 50th matching result.\n" + 
                                "There are more than 50 songs with this input.\n")
                    break

        if n == 0:              #Recommendations if lyrics not found
            return ("So sorry! '" + lyr + "' seems not to be found in any song inside our database.\n\n" +
                    "You could try with other lyrics, try these for example:\n" +
                    "'Push it out, fake a smile'\n" +
                    "'I just wanna stay in the sun where I find'")

        return res

            