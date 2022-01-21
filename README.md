# Music360 🔉

Music360 is a university project for the course Lab of Software Project Development, developed by "Git me 30L" group, composed by Marco Battiston, Mike Cecconello, Roberto Buiatti and Pietro Donati.
Let's have some fun!

##CSV file 📊
In order to store all the songs and authors, we selected a CSV file from Kaggle that acts as a big library of all the songs and authors, plus some additional informations. 
Before starting, we cleaned the dataset form less interesting variables, ending up with 16 variables from the initial 25.
We called it spotify_songs.csv, since we based it on this streaming platform. 

It is defined by the following properties:
Track ID
Track name
Track artist
Lyrics
Track album ID
Track album name
Track album release date
Playlist name
Playlist ID
Playlist genre
Playlist subgenre
Tempo
Duration ms
Language

The original file contains roughly 16 thousand different songs.


##Setting up ⚙️
Before you access our software, a bit of preparation is required.
First, by using the command git clone https://github.com/MarcoBattiston1/Music360.git in the terminal/command prompt of your PC, the entire folder containing all the modules and the files needed to run the program will automatically download. 
In case git is not already present in your device, please proceed with the installation.

This is the list of the needed libraries:

Pandas
Numpy


To flawlessly run our software, please run the command pip install “library_name” (or pip3 install “library_name”, depending on your python version) with both the above mentioned libraries. 


##Features 🪄
The aim of the project is to create an interactive library of songs and artists.
The user can access various informations like song infos, lyrics, discography and much more.

The functions get_discography, get_info, get_song are stored in their respective modules, while the function karaoke is stored in the same module of get_info. 
All functions are recalled in the main code.  These functions are then called by ArgParse that stores user inputs, subsequently main.py performs the process.




##Usage 🎸
Now let’s see some frequent user interaction examples: 

###SONG INFOS
For accessing information about a specific song, for example Party Rock Anthem, the command should be written as follows:

```bash
python main.py "Party Rock Anthem” 
```

###DISCOGRAPHY
This function will return the entire discography of the artist, in this case example, Mariah Carey.

```bash
python main.py -a “Mariah Carey” 
```
###KARAOKE
This karaoke function will return the entire lyrics of a specific song. It will also provide a copy-and-paste link for the Spotify version of the song, so the user can paste the link in his browser that will start playing the song on Spotify.

```bash
python main.py -k "Party Rock Anthem"
```

###FIND SONG
This function will solve a problem that all of us had at least once in our life. 
With just a few words from the lyrics of a song as input, the function will help the user to find that song and its artist.

```bash
python main.py -f "Push it out, fake a smile"
```


##Running Tests ☑️
In the folder Tests the user can find the unit tests. To perform tests, first make sure to be inside the directory Music360, then the command should be written as follows:

cd mypackage

python test.py


##CSV Source 📝
https://www.kaggle.com/imuhammad/audio-features-and-lyrics-of-spotify-songs


##Contributing 🤟🏼
Please contact us if you would like to contribute to this project. Feel free to expand or enhance current functionalities. 

##License 🔑
GNU License


##Authors 🧻
Marco Battiston
Roberto Buiatti
Mike Cecconello
Pietro Donati




