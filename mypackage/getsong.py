'''
This module contains a function named get_song,
which takes as input a string given by the user
and check if that string is present in any lyrics
present in the dataset, through an iteration.
The function returns all the matches find,
but stops at 50 songs in order to keep the output clear.
'''

class Lyrics:
    def __init__(self, lyr, path):
        self.lyr = lyr
        self.path = path

    def getsong(self):
        import pandas as pd
        lyr = str(self.lyr)
        lyr = self.lyr.lower()
        wrong_input = ["", " "]
        if str(lyr) in wrong_input:
            return "Empty input is not supported by the program. Try with something different!"
        db = pd.read_csv(self.path)
        all_lyr = list(db["lyrics"])
        for i in range(len(all_lyr)):
            all_lyr[i] = all_lyr[i].lower()
        n = 0
        if "mypackage" in self.path:
            print("This could take a while...\n")
        res = ""
        for i in range(len(all_lyr)):  # iterating through each lyrics of the dataset
            for j in range(len(all_lyr[i - len(lyr)])):  # accessing each set of words
                if lyr == all_lyr[i][j:j + len(lyr)]:
                    res += db["track_name"][i] + " - " + db["track_artist"][i]
                    n += 1
                    if n >= 50:
                        return (res + "\nExecution stopped at 50th matching result. " + 
                                "There are more than 50 songs with this input.\n")
                    return res

        if n == 0:
            return ("So sorry! '" + lyr + "' seems not to be found in any song inside our database.\n\n" +
                    "You could try with other lyrics, try these for example:\n" +
                    "'Push it out, fake a smile'\n" +
                    "'I just wanna stay in the sun where I find'")

            