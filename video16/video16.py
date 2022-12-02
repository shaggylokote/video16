coding: utf-8



Created on Thu May 5 14:40:38 2022

@author: nicosio

# Cuando trabajamos con variables en la clase, tenemos las variables de #instancia. Estas variables se reconocen por que tienen el prefijo self # y son las que hemos usado hasta el momento

# Tambien se tienen la variables de clase, que se definen y pertenecen a la # clase y no a la instacia. Estas variables existen idependientemente de #cuantas instancias se hayan creado

# Todos los objetos creados tienen acceso a las variables de clase #Usualmente se usan para definir una constante que todas las instancias puedan # usar, tambien para contadores o para tener un valor compartido entre todas # las instancias

#Funcionalmente se parecen a las variables estaticas de C#

# Se definen entre class y el primer def que tengamos

class cuentaBanco:

tipoCambio=20.22

def _init_(self, cantidad): self.cantidad-cantidad
def convertirDolares (self): print(self.cantidad/cuentaBanco.tipoCambio)

#Creamos un par de instancias

cuental=cuentaBanco (500)

cuenta2=cuentaBanco (2357)

# Invocamos el metodo

cuental.convertirDolares() cuenta2.convertirDolares()

print('')

# Hacemos el cambio a la variable de clase # El cambio es visto por todas las instancias

cuentaBanco.tipoCambio=18.57

# Invocamos el metodo

cuental.convertirDolares() cuenta2.convertirDolares()

print('------')
