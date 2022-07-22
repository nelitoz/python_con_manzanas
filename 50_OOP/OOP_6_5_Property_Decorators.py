import time

class Gift():
    _price = None
    def __init__(self, item):
        self.item = item
        
    def costly_computation(self):
        print ("Costly computation...")
        time.sleep(2)
        return 10
    
    @property
    def price(self):
        if not self._price:
            self._price = self.costly_computation()
        return self._price

