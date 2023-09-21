class MusicLibrary():
    def __init__(self):
        self.tracks = []
    
    def add(self, track):
        f_track = [track.title, track.artist]
        self.tracks.append(f_track)
        print(self.tracks)
    
    def search_for_word(self, word):
        matching_list = []
        for track in self.tracks:
            if word in track[0]:
                matching_list.append(track[0])
        return matching_list
    
    
