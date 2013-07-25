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
        self.status = 'ON'

    def off(self):
        self.status = 'OFF' 
    

class Dimmer(Lightswitch):
    def __init__(self, n, t):
        Lightswitch.__init__(self, n, t)
        self.brightness = 0

    def brighten(self, inc):
        if self.brightness < 255:
            self.brightness += 1
    
    def darken(self, dec):
        if self.brightness > 0:
            self.brightness -= 1

    def get_brightness(self):
        return self.brightness
    

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
    
    
        
