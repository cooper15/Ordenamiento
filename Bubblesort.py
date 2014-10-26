__author__ = 'cooper15'


class OrdemanientoBurbuja:
    def ordenar(self, lista_a_ordenar):
        temporal = 0
        tamanio_lista = len(lista_a_ordenar)
        for i in range(0, tamanio_lista):
            for j in range(0, tamanio_lista - 1):
                if lista_a_ordenar[j] > lista_a_ordenar[j + 1]:
                    temporal = lista_a_ordenar[j]
                    lista_a_ordenar[j] = lista_a_ordenar[j + 1]
                    lista_a_ordenar[j + 1] = temporal
        return lista_a_ordenar

    def mostrar_lista_or(self, lista_ordenada):
        print(lista_ordenada)

    def mostrar_lista_des(self, lista_sin_ordenar):
        print(lista_sin_ordenar)

lista = [3, 1, 2, 6, 3, 5]
objeto = OrdemanientoBurbuja()
objeto.mostrar_lista_des(lista)
lista_ordenada = objeto.ordenar(lista)
objeto.mostrar_lista_or(lista_ordenada)
