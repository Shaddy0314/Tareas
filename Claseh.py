class coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = 0
        self.encendido = False

    def encender(self):
        self.encendido = True
        return f"El coche {self.marca} {self.modelo} está encendido."   
    
    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            return f"El coche {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h."
        else:
            return f"El coche {self.marca} {self.modelo} está apagado. No puede acelerar."      
    
coche1 = coche("Toyota", "Corolla", 2020)
print(coche1.encender())
print(coche1.acelerar(50))
