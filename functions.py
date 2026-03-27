def add(a, b):
    return a + b  # No pasaba el test porque devuelve un string en lugar de un número


def divide(a, b):
    return (
        a / b
    )  # No pasaba el test porque hay un +1 en el divisor, lo que hace que el resultado sea incorrecto


def get_element(list_, index):
    return list_[
        index
    ]  # No pasaba el test porque pasa el indice +1, lo que devuelve el numero de la derecha


def convert_to_integer(value):
    return round(float(value))  # No pasaba el test porque faltaba el round
