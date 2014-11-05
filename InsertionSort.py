__author__ = 'cooper15'


class InsertionSort:
    def __init__(self):
        pass

    def insercion(self, lista_a_ordenar):
        """Ver definicion de algoritmo por inserción"""
        tamanio = len(lista_a_ordenar)
        for i in range(1, tamanio):
            temporal = lista_a_ordenar[i]
            j = i - 1
            while j >= 0:
                if temporal > lista_a_ordenar[j]:
                    lista_a_ordenar[j + 1] = temporal
                    break
                else:
                    lista_a_ordenar[j + 1] = lista_a_ordenar[j]
                j -= 1
            if j == -1:
                lista_a_ordenar[0] = temporal

        return lista_a_ordenar
lista = [9, 5, 8, 1, 3]
objeto = InsertionSort()
print(objeto.insercion(lista))