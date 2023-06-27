class Person:
    def __init__(self, name):
        self.name = name
     
    def talk(self):
        print(f"{self.name} speak english")


paavan = Person("Paavan")
paavan.talk()
