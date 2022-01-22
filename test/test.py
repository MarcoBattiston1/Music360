"""
This module is the one that tests some of the functions
necessary to let the user interact with the database.
Each Test Case tests a Known valid and invalid entries.
"""

import unittest
import sys
from getdiscography import Artist
from getinfo import Song
from getsong import Lyrics
sys.path.insert(0, '../modules/')


class TestInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_track_name(self):

        expected = ("\nThe song: 'My Body' is made by 'Hot Shade'." +
                    "\nIt was released in the album 'My Body'," +
                    " in the date 2017-09-29," +
                    " and it appeared in the spotify playlist" +
                    " named Tropical Beats," +
                    " with other song of genre latin, and subgenre tropical." +
                    "\nThe song has 104 bpm and it lasts 161 seconds.\n")

        a = Song("My Body", "../resources/spotify_songs.csv")
        b = a.getinfo()

        self.assertEqual(b, expected)

    # invalid inputs
    def test_incorrect_track_name(self):

        expected = (" The song you're looking for" +
                    " is not present in our database. " +
                    " Here you are some recommended songs we have:\n " +
                    " 'Party Rock Anthem',\n " +
                    " 'Symphony Of Destruction',\n " +
                    " 'Some Nights'! ")

        a = Song("My Bodi", "../resources/spotify_songs.csv")
        c = Song("99", "../resources/spotify_songs.csv")
        b = a.getinfo()
        d = c.getinfo()

        self.assertEqual(b, expected)
        self.assertEqual(d, expected)

    # corner case: empty string
    def test_empty_track_name(self):

        expected = (" The song you're looking for" +
                    " is not present in our database. " +
                    " Here you are some recommended songs we have:\n " +
                    " 'Party Rock Anthem',\n " +
                    " 'Symphony Of Destruction',\n " +
                    " 'Some Nights'! ")

        a = Song(" ", "../resources/spotify_songs.csv")
        b = a.getinfo()

        self.assertEqual(b, expected)

    # smoke test: valid inputs
    def test_correct_artist_name(self):

        expected = ("\nMariah Carey made the following songs:" +
                    "\n\nAll I Want for Christmas Is You" +
                    "\nEmotions\nAlways Be My Baby\nObsessed\nSomeday" +
                    "\nMake It Happen\nYou're So Cold\nDreamlover" +
                    "\nThank God I Found You (feat. Joe & Nas)" +
                    " - Make It Last Remix Edit\nFantasy\nOne Sweet Day")

        a = Artist("Mariah Carey", "../resources/spotify_songs.csv")
        b = a.getdiscography()

        self.assertEqual(b, expected)

    # invalid inputs
    def test_incorrect_artist_name(self):

        expected = (" The artist you're looking for" +
                    " is not present in our database. " +
                    " Here you are some recommended artist we have:\n " +
                    " 'Mariah Carey',\n " +
                    " 'Madison Beer',\n " +
                    " 'GASHI'! ")

        a = Artist("Maria Carey", "../resources/spotify_songs.csv")
        c = Artist("85", "../resources/spotify_songs.csv")
        b = a.getdiscography()
        d = c.getdiscography()

        self.assertEqual(b, expected)
        self.assertEqual(d, expected)

    # corner case: empty string
    def test_empty_artist_name(self):

        expected = (" The artist you're looking for" +
                    " is not present in our database. " +
                    " Here you are some recommended artist we have:\n " +
                    " 'Mariah Carey',\n " +
                    " 'Madison Beer',\n " +
                    " 'GASHI'! ")

        a = Artist(" ", "../resources/spotify_songs.csv")
        b = a.getdiscography()

        self.assertEqual(b, expected)

    # smoke test: valid inputs
    def test_correct_karaoke_song(self):

        expected = (" \nType this in your favourite browser: 'spotify:track:" +
                    '0IkKz2J93C94Ei4BvDop7P' +
                    "' and sing with our lyrics!\n\n " +
                    'PARTY ROCK ANTHEM' + " - " + 'LMFAO' + "\n\n" +
                    "Party Rock Yeah Whoo! Let's go!" +
                    " Party rockers in the house tonight" +
                    " Everybody just have a good time (Yeah)" +
                    " And we gon' make you lose your mind (Whoo!)" +
                    " Everybody just have a good time (Clap!)" +
                    " Party rockers in the house tonight (Oh!)" +
                    " Everybody just have a good time (I can feel it, baby!)" +
                    " And we gon' make you lose your mind (Yeah)" +
                    " We just wanna see you...Shake that! In the club:" +
                    " Party rock Looking for your girl? She on my jock (Huh)" +
                    " Non-stop when we in the spot Booty" +
                    " moving weight like she on the block (Whoo!)" +
                    " Where the drank? I gots to know Tight jeans, tattoo," +
                    " 'cause I'm rock and roll Half-black, half-white:" +
                    " domino Gainin' money. Oprah, dough Yo!" +
                    " I'm running through these hoes like Drano" +
                    " I got that devilish flow rock and roll no halo," +
                    " we party rock! Yeah, that's the crew that" +
                    " I'm reppin'On the rise to the top," +
                    " no Led in our Zeppelin (Hey!)" +
                    " Party rockers in the house tonight (Whoo!)" +
                    " Everybody just have a good time (Yeah)" +
                    " And we gon' make you lose your mind" +
                    " Everybody just have a good time (Let's go!)" +
                    " Party rockers in the house tonight" +
                    " Everybody just have a good time (I can feel it, baby!)" +
                    " And we gon' make you lose your mind" +
                    " We just wanna see you..." +
                    "Shake that!Every day I'm shufflin' (Shake)" +
                    " Shufflin', shufflin' (Shake)" +
                    " Step up fast and be the first girl" +
                    " to make me throw this cash We get money don't be mad," +
                    " now stop - hatin' is bad One more shot for us" +
                    " (Another round!)" +
                    " Please fill up my cup (Don't mess around!)" +
                    " We just wanna see (You shake it now!)" +
                    " Now you wanna be (You're naked now!)" +
                    " Get up, get down, put your hands up to the sound" +
                    " Get up," +
                    " get down, put your hands up to the sound" +
                    " Get up, get down," +
                    " put your hands up to the sound (Whoo!)" +
                    " Put your hands up to the sound" +
                    " Put your hands up to the sound (Let's go!)" +
                    " Get up, get up, get up Get up, get up, get up" +
                    " Get up, get up, get up" +
                    " Put your hands up to the sound To the sound" +
                    " Put your hands up (Whoo!) Put your hands up" +
                    " Put your hands up Put your hands up" +
                    " Party rockers in the house tonight" +
                    " (Put your hands up, whoo!)" +
                    " Everybody just have a good time" +
                    " (Put your hands up)" +
                    " And we gon' make you lose your mind" +
                    " (Put your hands up)" +
                    " Everybody just have a good, good," +
                    " good time Oh-oh-oh-oh-oh" +
                    " (Put your hands up) Oh-oh-oh-oh-oh" +
                    " (I can feel it, baby!)" +
                    " Oh-oh-oh-oh-oh (Put your hands up)" +
                    " Oh-oh-oh-oh-oh (Put your hands up)" +
                    " Shake that!Every day I'm shu-shufflin'" +
                    " Put yo', Put yo' (Hands up) Put yo', Put yo' (Yeah)" +
                    " Put yo', Put yo' (Whoo!)" +
                    " Hands up Put yo', Put yo' (Hands up)" +
                    " Put your hands up Put your hands up" +
                    " Put your hands up Party Rock Yeah Whoo! Let's go!" +
                    " Party rockers in the house tonight" +
                    " Everybody just have a good time (Yeah)" +
                    " And we gon' make you lose your mind (Whoo!)" +
                    " Everybody just have a good time (Clap!)" +
                    " Party rockers in the house tonight (Oh!)" +
                    " Everybody just have a good time (I can feel it, baby!)" +
                    " And we gon' make you lose your mind (Yeah)" +
                    " We just wanna see you...Shake that! In the club:" +
                    " Party rock Looking for your girl? She on my jock (Huh)" +
                    " Non-stop when we in the spot" +
                    " Booty moving weight like she on the block (Whoo!)" +
                    " Where the drank? I gots to know Tight jeans, tattoo," +
                    " 'cause I'm rock and roll Half-black, half-white:" +
                    " domino Gainin' money. Oprah, dough Yo!" +
                    " I'm running through these hoes like Drano" +
                    " I got that devilish flow rock and roll no halo," +
                    " we party rock! Yeah, that's the crew that" +
                    " I'm reppin'On the rise to the top," +
                    " no Led in our Zeppelin (Hey!)" +
                    " Party rockers in the house tonight (Whoo!)" +
                    " Everybody just have a good time (Yeah)" +
                    " And we gon' make you lose your mind" +
                    " Everybody just have a good time (Let's go!)" +
                    " Party rockers in the house tonight" +
                    " Everybody just have a good time" +
                    " (I can feel it, baby!)" +
                    " And we gon' make you lose your mind" +
                    " We just wanna see you...Shake that!" +
                    "Every day I'm shufflin' (Shake)" +
                    " Shufflin', shufflin' (Shake)" +
                    " Step up fast and be the first girl" +
                    " to make me throw this cash We get money don't be mad," +
                    " now stop - hatin'" +
                    " is bad One more shot for us (Another round!)" +
                    " Please fill up my cup" +
                    " (Don't mess around!)" +
                    " We just wanna see (You shake it now!)" +
                    " Now you wanna be (You're naked now!)" +
                    " Get up, get down," +
                    " put your hands up to the sound Get up," +
                    " get down, put your hands up to the sound Get up," +
                    " get down, put your hands up to the sound (Whoo!)" +
                    " Put your hands up to the sound" +
                    " Put your hands up to the sound (Let's go!)" +
                    " Get up, get up, get up Get up, get up, get up Get up," +
                    " get up, get up Put your hands up to the sound" +
                    " To the sound Put your hands up (Whoo!)" +
                    " Put your hands up Put your hands up" +
                    " Put your hands up Party rockers in the house tonight" +
                    " (Put your hands up, whoo!)" +
                    " Everybody just have a good time" +
                    " (Put your hands up) And we gon'" +
                    " make you lose your mind (Put your hands up)" +
                    " Everybody just have a good, good," +
                    " good time Oh-oh-oh-oh-oh (Put your hands up)" +
                    " Oh-oh-oh-oh-oh (I can feel it, baby!)" +
                    " Oh-oh-oh-oh-oh (Put your hands up)" +
                    " Oh-oh-oh-oh-oh (Put your hands up)" +
                    " Shake that!Every day I'm shu-shufflin'" +
                    " Put yo', Put yo' (Hands up) Put yo', Put yo' (Yeah)" +
                    " Put yo', Put yo' (Whoo!) Hands up" +
                    " Put yo', Put yo' (Hands up)" +
                    " Put your hands up Put your hands up" +
                    " Put your hands up")

        a = Song("Party Rock Anthem", "../resources/spotify_songs.csv")
        b = a.karaoke()

        self.assertEqual(b, expected)

    # invalid inputs
    def test_incorrect_karaoke_song(self):

        expected = ("Not found!\nHere you are some recommended songs" +
                    " we have:\n" +
                    "'Party Rock Anthem',\n" +
                    "'Symphony Of Destruction',\n" +
                    "'Some Nights'!")

        a = Song("Party Rock Antem", "../resources/spotify_songs.csv")
        c = Song("85", "../resources/spotify_songs.csv")
        b = a.karaoke()
        d = c.karaoke()

        self.assertEqual(b, expected)
        self.assertEqual(d, expected)

    # corner case: empty string
    def test_empty_karaoke_name(self):

        expected = ("Not found!\nHere you are some recommended songs" +
                    " we have:\n" +
                    "'Party Rock Anthem',\n" +
                    "'Symphony Of Destruction',\n" +
                    "'Some Nights'!")

        a = Song(" ", "../resources/spotify_songs.csv")
        b = a.karaoke()

        self.assertEqual(b, expected)

    # smoke test: valid inputs
    def test_correct_get_song(self):

        expected = ("STORY OF A LONELY GUY" + " - " + "BLINK-182\n")

        a = Lyrics("Push it out, fake a smile", "../resources/spotify_songs.csv")
        b = a.getsong()

        self.assertEqual(b, expected)

    # invalid inputs
    def test_incorrect_get_song(self):

        expected = ("So sorry! '" +
                    "push it out, fake smile" +
                    "' seems not to be found in any song" +
                    " inside our database.\n\n" +
                    "You could try with other lyrics," +
                    " try these for example:\n" +
                    "'Push it out, fake a smile'\n" +
                    "'I just wanna stay in the sun where I find'")

        a = Lyrics("Push it out, fake smile", "../resources/spotify_songs.csv")
        b = a.getsong()

        self.assertEqual(b, expected)

    # corner case: empty string
    def test_empty_get_song(self):

        expected = ("Empty input is not supported by the program." +
                    " Try with something different!")

        a = Lyrics(" ", "../resources/spotify_songs.csv")
        b = a.getsong()

        self.assertEqual(b, expected)


if __name__ == "__main__":
    unittest.main()
