class Location():
    def __init__(self, n):
        self.name = n
        
    def rename(self, n):
        self.name = n 
        
    def get_name(self):
        return self.name
     

class Room(Location):
    pass

class Floor(Location):
    pass


        