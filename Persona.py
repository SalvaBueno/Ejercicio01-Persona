import random

class Persona():
    def __init__(self,nombre="", edad = 0, sexo="H", peso="0", altura="0"):
            self.introducirSexo(sexo)
            self.__nombre = nombre
            self.__edad = int(edad)
            self.__DNI = ''
            self.__sexo = sexo
            self.__peso = int(peso)
            self.__altura = int(altura)
            self.generarDNI()


    def calcularIMC(self):
        peso =self.__altura
        altura=self.__peso
        PI = (peso/(altura^2))

        if(PI==self.__peso):
            print ('Peso Ideal')
            return 0
        else:
            if(PI>self.__peso):
                print ('No llegas a tu peso ideal')
                return -1
            else:
                print ('Sobre Peso')
                return 1

    def esMayorDeEdad(self):
        if self.__edad>17:
            return True
        else:
            return False

    def introducirSexo(self,sexo):
        if sexo != 'M' and sexo != 'H':
            sexo = 'M'

    def toString(self):
        print('')
        print ('Nombre: '+self.__nombre)
        print ('Edad: ' + str(self.__edad))
        print ('DNI: ' + self.__DNI)
        print ('Sexo: ' +self.__sexo)
        print ('Peso: '+ str(self.__peso))
        print ('Altura: ' + str(self.__altura))
        print('')

    def generarDNI(self):
        diccionario = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X",
                       11: "B", 12: "N", 13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L",
                       20: "C", 21: "K", 22: "E"}
        x=[]
        i=0
        while(i<8):
            x.append(random.randint(0,9))
            i += 1

        x2=str(x[0])+str(x[1])+str(x[2])+str(x[3])+str(x[4])+str(x[5])+str(x[6])+str(x[7])
        resto = int(x2)%23
        letra=diccionario[resto]
        self.__DNI = x2+letra


    def setNombre(self, nombre):
        self.__nombre = nombre
    def setEdad(self, edad):
        self.__edad = int(edad)
    def setSexo(self, sexo):
        self.__sexo = sexo
    def setPeso(self, peso):
        self.__peso = int(peso)
    def setAltura(self, altura):
        self.__altura = int(altura)

