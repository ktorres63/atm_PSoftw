class Cajero:
    def __init__(self):
        self.continuar = True
        self.monto = 5000
        self.opciones = 0

    def passw(self):
        return 1234

    def contraseña(self):
        contador = 1
        while contador <= 3:
            x = int(input("ingrese su contraseña:" ))
            if x == self.passw():
                print("Contraseña Correcta")
                break
            else:
                print(f"Contraseña Incorrecta, le quedan {3 - contador} intentos")
                if contador == 3:
                    print("No puede realizar operaciones.")
                    self.continuar = False
                contador+=1


    def depositar(self,dep):
        if dep > 0:
	        self.monto+=dep
        

    def retiro(self,reti):
        if 0 < reti < self.monto:
            self.monto-=reti

    def ver(self):
        return self.monto



    def menu(self):
        opcion = 0
        while opcion != "4":
            print(""" Bienvenido al cajero automatico
            ******Menú******
            1-  Depositar
            2- Retirar
            3- Ver saldo
            4- Salir """)
            opcion = input("Su opción es: ")
            if self.continuar:
                if opcion == "1" :
                    dep = int(input("Ingrese su monto a depositar:"))
                    print("Usted a depositado",dep)
                    self.depositar(dep)
                    print("Su nuevo saldo es" ,self.ver())

                elif opcion == "2" :
                    retirar=int(input("¿Cuánto desea retirar? : "))
                    print("Su monto actual es", self.ver())

                    if  retirar <= self.monto:    #girar =5000
                        self.retiro(retirar)
                        print("Usted a retirado:", retirar , "su nuevo monto es", self.ver())
                    else:
                        print("Imposible realizar el retiro, su monto es menor")

                elif opcion == "3":
                    print("Su saldo es: " , self.ver())
                elif opcion == "4":
                    print("Programa finalizado")
                else:
                    print("NO existe esa opción")
            else:
                if opcion in "123":
                    print("Imposible realizar esa operación")
                elif opcion == "4":
                    print("Programa finalizado")
                else:
                    print("No existe esa opción")


