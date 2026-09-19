# Laboratorio 2 — Árbol de Merkle

**Estudiante:** Karelyn Caicedo Vélez

## Contenido del Repositorio

- Código fuente en lenguaje de programación python Laboratorio2.py.
- Captura de Pantalla del Diagrama del árbol construido por el mismo código.
- Captura de Pantalla de las verificaciones.
- Y este README.

## Uso de IA generativa

Se usó un asistente de IA específicamente Claude para ayudar a construir el código y verificarlo.

Se usó para ayudar a diseñar prácticamente la prueba de inclusión, específicamente la parte de
generar_prueba, verificar_prueba e imprimir_diagrama, y un poco en la parte del experimento.

Yo una parte del código, específicamente la parte del principio, la de construir_arbol, la 
reutilice porque ya la había creado con ayuda de la IA desde la clase donde lo vimos y lo 
construimos, e hice gran parte del final, la del experimento, donde escribí las transacciones y lo 
que se imprimia en los resultados, también revisé el código y lo probé y estuve activa en todo mi 
proceso de aprendizaje junto a la IA.

## Cómo correrlo

Se necesita tener python instalado.

Y ya se corre dependiendo del sistema que tengamos de esta manera:

```
python Laboratorio2.py    (Windows)
python3 Laboratorio2.py   (Mac/Linux)
```

## Qué hace

El código construye un árbol de Merkle a partir de transacciones:

- Cada hoja es el hash SHA-256 de una transacción.
- Cada nodo de arriba es el hash de sus dos hijos combinados.
- Si sobra una hoja sin pareja, se duplica.
- También genera y verifica una prueba de inclusión que sirve para confirmar que una transacción sí pertenece al árbol, sin necesitar las demás transacciones.

## Qué hace el experimento

Al correrlo, el programa:

- Muestra las 5 transacciones y el árbol construido con su raíz.
- Modifica una transacción y muestra que la raíz cambia.
- Genera la prueba de inclusión de la transacción 3 y la verifica (da VALIDA).
- Prueba la verificación con un dato falso (da INVALIDA).
