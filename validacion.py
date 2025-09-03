from parde_peter import seleccionarPalabra, agregarPalabra

intentos_restantes = 5
palabra_actual = ""
descripcion_actual = ""

def nuevaPalabra():
    global palabra_actual, descripcion_actual, intentos_restantes
    p = seleccionarPalabra()
    if p:
        palabra_actual = p[1]
        descripcion_actual = p[2]
        intentos_restantes = 5
        return palabra_actual, descripcion_actual, intentos_restantes
    else:
        return None, None, 0

def verificarPalabra(usuario):
    global intentos_restantes, palabra_actual
    if usuario.lower() == palabra_actual.lower():
        return True, "¡Felicidades! Adivinaste la palabra."
    else:
        intentos_restantes -= 1
        if intentos_restantes == 0:
            mensaje = f"Perdiste. La palabra era: {palabra_actual}"
            return False, mensaje
        else:
            return False, f"Palabra incorrecta. Intentos restantes: {intentos_restantes}"

def agregarPalabraLogica(palabra, descripcion):
    if not palabra.strip() or not descripcion.strip():
        return False, "Por favor complete todos los campos."
    agregarPalabra(palabra.strip(), descripcion.strip())
    return True, "Palabra agregada con éxito."
