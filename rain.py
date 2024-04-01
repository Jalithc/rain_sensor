"""Class for rain sensor with 0.5 rain chance with __init__"""
class RainSensor:
    def __init__(self, rain_chance = 0.5):
        self.rain_chance = rain_chance
        self.is_wiper_on = True

    def wiper_turned_on(self, chance):
        if chance > self.rain_chance:
            print("Wiper turned on!")
            return self.is_wiper_on
        else:
            print("Wiper turned off!")
            return not self.is_wiper_on
        
rain = RainSensor()
rain.wiper_turned_on(0.4)
