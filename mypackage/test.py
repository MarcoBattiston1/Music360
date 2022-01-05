"""
This module is the one that tests some of the functions
necessary to let the user interact with the database.
Each Test Case tests a Known valid and invalid entries.

"""

import unittest
from getinfo import Song


class TestInput(unittest.TestCase):

    def setUp(self):
        self.T_track_name = "Party Rock Anthem"
    
    # smoke test: valid inputs
    def test_correct_track_name(self):
        
        expected = print("The song: '", 'Party Rock Anthem',"' is made by '",
                     'LMFAO', "'. It was released in the album '",
                      'Sorry For Party Rocking', "', in the date", 
                      "2011-01-01", ", and it appeared in the spotify playlist named",
                      "'Dr. Q's Prescription Playlist'", ", with other song of genre",
                     'pop', ", and subgenre",
                     'post-teen pop',". The song has",
                     "130","bpm and it lasts",
                     "262","seconds.")

        self.assertEqual((Song().getinfo(self.T_track_name)), expected)
