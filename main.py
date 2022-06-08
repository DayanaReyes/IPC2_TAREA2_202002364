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
    def imprimir(self):
        aux=self.primero
        while aux!=None:
            print(aux.dato)
            aux=aux.siguiente
            if aux==self.primero:
                break