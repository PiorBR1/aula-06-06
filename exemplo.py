class Animal:
    def __init__(self, nome):
        self.nome = nome
    def emite_som (self):
        print ("esse animal emite um som")
class cachorro (Animal):
    def emite_som(self):
        print(f'"{self.nome} diz: au au"')
class gato(Animal):
    def emite_som(self):
        print(f'"{self.nome} diz: Miau"')
#Teste

rex = cachorro("Rex")
rex.emite_som()
mike = gato("mike")
mike.emite_som()
    
        
