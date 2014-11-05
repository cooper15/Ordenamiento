__author__ = 'cooper15'


class QuickSort:
    def __init__(self):
        pass
    # Los parámetros p_inferior y p_superior representan los valores extremos de la lista o sublista.

    def ordenamiento(self, lista_a_ordenar, p_inferior, p_superior):
        pivote = lista_a_ordenar[p_superior/2]  # Se escoje un valor central como pivote.es mala idea tomar los extremos
        i_izquierdo = p_inferior
        j_derecho = p_superior
        while i_izquierdo < j_derecho:
            while lista_a_ordenar[i_izquierdo] < pivote:
                i_izquierdo += 1
            while lista_a_ordenar[j_derecho] > pivote:
                j_derecho -= 1
            if i_izquierdo <= j_derecho:
                temporal = lista_a_ordenar[i_izquierdo]
                lista_a_ordenar[i_izquierdo] = lista_a_ordenar[j_derecho]
                lista_a_ordenar[j_derecho] = temporal
        if j_derecho > p_inferior:
            self.ordenamiento(lista_a_ordenar, p_inferior, i_izquierdo -1)
        if i_izquierdo < p_superior:
            self.ordenamiento(lista_a_ordenar, i_izquierdo + 1, p_superior)
        return lista_a_ordenar

lista = [9, 5, 8, 1, 3]
quick_sort = QuickSort()
print(quick_sort.ordenamiento(lista, 0, 4))


