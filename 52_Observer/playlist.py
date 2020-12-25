#Publisher
# Obserbable

class Playlist:
    def __init__(self):
        self.tracklist = []
        self._observers_list = []
    
    def add_track(self, track):
        self.tracklist.append(track)
        self._notify()
    
    def _notify(self):
        for observer in self._observers_list:
            observer.update(self)
    
    def get_state(self):
        return self.tracklist
    
    def attach(self,observer):
        self._observers_list.append(observer)

class Jazz(Playlist):
    pass

class Funk(Playlist):
    pass

class Rock(Playlist):
    pass
