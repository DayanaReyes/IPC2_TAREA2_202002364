class Nodo():
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None
class Lista():
    def __init__(self):
        self.primero=None
        self.ultimo=None
    def AgregarFinal(self,dato):
        nuevo= Nodo(dato)
        if self.primero==None:
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            auxiliar=self.ultimo
            auxiliar.siguiente=nuevo
            self.ultimo=nuevo
            self.ultimo.anterior=auxiliar
        self.primero.anterior=self.ultimo
        self.ultimo.siguiente=self.primero
    def buscar(self,numero):
        aux=self.primero
        while aux!=None:
            if aux.dato==numero:
                print("anterior:",aux.anterior.dato,", actual:",aux.dato,", siguiente:",aux.siguiente.dato)
                break
            aux=aux.siguiente
    def imprimir(self):
        aux=self.primero
        while aux!=None:
            print(aux.dato)
            aux=aux.siguiente
            if aux==self.primero:
                break
listanumeros=Lista()
listanumeros.AgregarFinal(7)
listanumeros.AgregarFinal(96)
listanumeros.AgregarFinal(72)
listanumeros.AgregarFinal(10)
listanumeros.AgregarFinal(25)
listanumeros.AgregarFinal(18)
listanumeros.AgregarFinal(2)
print("Lista de numeros: ")
listanumeros.imprimir()
numero=int(input("Ingrese numero: "))
listanumeros.buscar(numero)