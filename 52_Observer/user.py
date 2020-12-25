#Suscriber
# Observer

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class User(Observer):
    def __init__(self,username):
        self.username = username
        self.tracklist = []
    
    def update(self, publisher):
        print (f">> Updating user {self.username}")
        state = publisher.get_state()
        self.tracklist.append(state)
    
    def play_songs(self):
        print(f"Playing {self.tracklist} to {self.username}")

