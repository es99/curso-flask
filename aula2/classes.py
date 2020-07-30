class Animal():
    # atributos de classe
    planeta = "Terra"
    _animal_nasceu = False

    @property
    def nasceu(self):
        return self._animal_nasceu

    #método
    def nascer(self):
        self._animal_nasceu = True
        print(f"Oi eu nasci no planeta {self.planeta}")

    def comer(self):
        print("Estou comendo.. crunch.. crunch")

class Mamifero(Animal):
    def comer(self):
        print("Estou tomando leite")

class Oviparos(Animal):
    def nascer(self):
        print(f"Acabei de quebrar o povo no {self.planeta}")

class Especial(Mamifero, Oviparos):
    def nadar(self):
        print("Tchibum")