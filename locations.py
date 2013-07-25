class Location():
    def __init__(self, n):
        self.name = n
        
    def rename(self, n):
        self.name = n 
        
    def get_name(self):
        return self.name
     

class Room(Location):
    def __init__(self, n):
        self.name = n
        self.devices = []
        
    def add_device(self, d):
        self.devices.append(d)

    def get_devices(self):
        return self.devices
    
    def all_on(self):
        for d in self.devices:
            if d.type == 'switch':
                d.on()
                
    def all_off(self):
        for d in self.devices:
            if d.type == 'switch':
                d.off()
        
        
class Floor(Location):
    def __init__(self, n):
        self.name = n
        self.rooms = []
        
    def add_room(self, r):
        self.rooms.append(r)
        
    def get_rooms(self):
        return self.rooms
    
    def all_on(self):
        for r in self.rooms:
            r.all_on()
            
    def all_off(self):
        for r in self.rooms:
            r.all_off()
            



        