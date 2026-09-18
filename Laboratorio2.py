import hashlib
 
def sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()
 
def construir_arbol(transacciones):
    nivel = [sha256(tx) for tx in transacciones]   # hojas: hash de cada transaccion
    arbol = [nivel]                                # guardamos todos los niveles para verlos
 
    while len(nivel) > 1:
        # si el nivel tiene un numero impar de elementos, se duplica el ultimo
        actual = nivel + [nivel[-1]] if len(nivel) % 2 == 1 else nivel
        siguiente = []
        for i in range(0, len(actual), 2):
            siguiente.append(sha256(actual[i] + actual[i + 1]))   # combina de a pares
        arbol.append(siguiente)
        nivel = siguiente
 
    return arbol
 
def generar_prueba(arbol, indice):
    prueba = []
    idx = indice
 
    for nivel in arbol[:-1]:   # todos los niveles menos la raiz
        es_ultimo_impar = (idx == len(nivel) - 1) and (len(nivel) % 2 == 1)
 
        if es_ultimo_impar:
            hermano = nivel[idx]        # se empareja con su propia copia duplicada
            posicion = "derecha"
        elif idx % 2 == 0:
            hermano = nivel[idx + 1]
            posicion = "derecha"
        else:
            hermano = nivel[idx - 1]
            posicion = "izquierda"
 
        prueba.append((hermano, posicion))
        idx = idx // 2
 
    return prueba
 
def verificar_prueba(hash_hoja, prueba, raiz):
    actual = hash_hoja
    for hermano, posicion in prueba:
        if posicion == "derecha":
            actual = sha256(actual + hermano)
        else:
            actual = sha256(hermano + actual)
    return actual == raiz

def imprimir_diagrama(arbol):
    ultimo_nivel = len(arbol) - 1
    for n in reversed(range(len(arbol))):
        if n == ultimo_nivel:
            etiqueta = "Raiz"
        elif n == 0:
            etiqueta = "Hojas"
        else:
            etiqueta = f"Nivel {n}"
        hashes_cortos = [h[:8] for h in arbol[n]]
        print(f"{etiqueta}: {hashes_cortos}")

# EXPERIMENTO
if __name__ == "__main__":
 
    transacciones = [
        "T1: Ana paga 50 a Luis",
        "T2: Luis paga 20 a Carla",
        "T3: Carla paga 15 a Ana",
        "T4: Ana paga 30 a Pedro",
        "T5: Pedro paga 10 a Luis",
    ]
 
    print("Transacciones:")
    for i, tx in enumerate(transacciones):
        print(f"[{i}] {tx}")
 
    # Construir el arbol y mostrar la raiz
    print("\nDiagrama del arbol de Merkle")
    arbol = construir_arbol(transacciones)
    imprimir_diagrama(arbol)
    raiz_original = arbol[-1][0]
    print(f"\nRaiz de Merkle: {raiz_original}")
 
    # Modificar una transaccion y demostrar que la raiz cambia
    print("\nModificando una transaccion")
    transacciones_mod = transacciones.copy()
    transacciones_mod[1] = "T2: Luis paga 999 a Carla"   # dato alterado
    print(f"Antes: {transacciones[1]}")
    print(f"Ahora: {transacciones_mod[1]}")
 
    arbol_mod = construir_arbol(transacciones_mod)
    raiz_mod = arbol_mod[-1][0]
    print(f"\nRaiz original: {raiz_original}")
    print(f"Raiz nueva: {raiz_mod}")
    print(f"¿La raiz cambio? {raiz_original != raiz_mod}")
 
    # Prueba de inclusion para la transaccion 3
    print("\nPrueba de inclusion para la transaccion 3")
    indice = 2
    prueba = generar_prueba(arbol, indice)
    hash_hoja_real = sha256(transacciones[indice])
 
    print(f"Transaccion: {transacciones[indice]}")
    print(f"Prueba (hermanos en el camino a la raiz): {[(h[:8], pos) for h, pos in prueba]}")
 
    print("\nVerificacion con el dato CORRECTO:")
    valida = verificar_prueba(hash_hoja_real, prueba, raiz_original)
    print(f"Resultado -> {'VALIDA' if valida else 'INVALIDA'}")
 
    print("\nVerificacion con un dato INCORRECTO (para probar que falla):")
    hash_hoja_falso = sha256("T3: dato incorrecto")
    invalida = verificar_prueba(hash_hoja_falso, prueba, raiz_original)
    print(f"Resultado -> {'VALIDA' if invalida else 'INVALIDA'}")