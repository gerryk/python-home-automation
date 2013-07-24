class Device():
    '''Device base class
    Class from which all automatable devices are inherited.
    Provides common aspects of automatable devices: name, type, status and a global address list
    '''
    def __init__(self, n, t):
        self.name = n
        self.type = t
        self.status = 'OFF'
        self.command = ''   
        
    def get_status(self):
        return self.status



class Lightswitch(Device):
    def on(self):
        pass
    
    def off(self):
        pass
    
    
class Dimmer(Lightswitch):
    def brighten(self, inc):
        pass
    
    def darken(self, dec):
        pass
    
    
class Relay(Device):
    def on(self):
        pass
    
    def off(self):
        pass
    
class Sensor(Device):
    pass

class Thermostat(Sensor):
    pass

class LightSensor(Sensor):
    pass

class IRSensor(Sensor):
    pass

class PressureSensor(Sensor):
    pass
    
    
        