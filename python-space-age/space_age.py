



class SpaceAge:

    def __init__(self, age):
        self.seconds = age


    def on_earth(self):
        seconds_on_earth = self.seconds
        age_on_earth = seconds_on_earth / (365.25*24*60*60)
        return round(age_on_earth, 2)

    def on_mercury(self):
        mercury = 0.2408467
        # COACHES' NOTE: this repeated action of calculating the age on earth could use its own function. Remember: repetition? -> function
        age_on_earth = self.seconds / (365.25*24*60*60)
        age_on_mercury = age_on_earth * mercury
        return round(age_on_mercury, 2)

    def on_venus(self):
        venus = 0.61519726
        age_on_earth = self.seconds / (365.25*24*60*60)
        age_on_venus = age_on_earth * venus
        return round(age_on_venus, 2)

    def on_mars(self):
        mars = 1.8808158
        age_on_earth = self.seconds / (365.25*24*60*60)
        age_on_mars = age_on_earth * mars
        return round(age_on_mars, 2)

    def on_jupiter(self):
        jupiter = 11.862615
        age_on_earth = self.seconds / (365.25*24*60*60)
        age_on_jupiter = age_on_earth * jupiter
        return round(age_on_jupiter, 2)

    def on_saturn(self):
        saturn = 29.447498
        age_on_earth = self.seconds / (365.25*24*60*60)
        age_on_saturn = age_on_earth * saturn
        return round(age_on_saturn, 2)

    def on_uranus(self):
        uranus = 84.016846
        age_on_earth = self.seconds / (365.25*24*60*60)
        age_on_uranus = age_on_earth * uranus
        return round(age_on_uranus, 2)


    def on_neptune(self):
        neptune = 164.79132
        age_on_earth = self.seconds / (365.25*24*60*60)
        age_on_neptune = age_on_earth * neptune
        return round(age_on_neptune, 2)

# COACHES' NOTE: Pretty much perfect.
