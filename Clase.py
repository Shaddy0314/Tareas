class superheroe:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder
        self.color_traje = "Rojo"
        self.fuerza = 100

    def user_poder(self):
            self.fuerza += 50
            return f"{self.nombre} ha usado su poder {self.poder} y ahora tiene una fuerza de {self.fuerza}."   
        
superheroe1 = superheroe("Superman", "Vuelo")
print(superheroe1.user_poder())

superheroe2 = superheroe("Batman", "Inteligencia")
print(superheroe2.user_poder())

