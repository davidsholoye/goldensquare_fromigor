1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE

class MusicTracker():
    def __init__(self):
        returns: nothing
        side-effects: creates an empty list for songs
    
    def add(self, song):
        song: string representing the name of a song
        return: string confirming either 'Song added' or 'Song already in list'
        side effects: adds song to the song_list if its not there already
    
    def list_of_song(self):
        returns: a list of the songs user has already listened to



3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLE

***
Given song
Adds song to list
returns list
***
tracker = MusicTracker()
tracker.add('Vienna')
tracker.list_of_songs()
=> "Songs you've listened to: Vienna"

***
Given empty string, does not add to list
Returns list w/o empty string
***
tracker = MusicTracker()
tracker.add('Macarena')
tracker.add("")
tracker.list_of_songs()
=> "Songs you've listened to: Macarena"

***
Printing List of songs without adding any songs
raises error message
***
tracker = MusicTracker()
tracker.list_of_songs()
=> 'ERROR! NO SONGS HERE YET!!!'

***
Adding repeated song
raises error message
***
tracker = MusicTracker()
tracker.add('Patience')
tracker.add('Patience')
=>'ERROR! SONG ALREADY IN LIST!'

***
Adding wrong data type
Consider it a string and add it
Prints it in the list
***
tracker = MusicTracker()
tracker.add(1997)
tracker.add(True)
tracker.list_of_songs()
=>"Songs you've listened to: 1997, True"
