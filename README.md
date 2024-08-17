# Algoritmo fuerza bruta simple (Python)

Este script Python implementa un ataque de fuerza bruta para descifrar contraseñas de 4 letras minúsculas.

## Descripción

El programa solicita al usuario una contraseña de 4 letras y luego genera sistemáticamente todas las combinaciones posibles de 4 letras minúsculas, comparándolas con la contraseña ingresada hasta encontrar una coincidencia.

## Características

-   **Validación de entrada:** Asegura que el usuario ingrese una contraseña de exactamente 4 letras.
-   **Generación de combinaciones:** Utiliza bucles anidados para crear todas las posibles combinaciones de 4 letras minúsculas.
-   **Comparación y salida:** Compara cada combinación generada con la contraseña objetivo y muestra la combinación actual en la consola.
-   **Medición de tiempo:** Registra el tiempo transcurrido desde el inicio del ataque hasta que se encuentra la contraseña.
-   **Terminación:** El programa finaliza automáticamente cuando se encuentra la contraseña o el usuario puede presionar Enter para comenzar el ataque.

## Librerías Utilizadas

-   `time`: Para medir el tiempo de ejecución.
-   `sys`: Para terminar el programa cuando se encuentra la contraseña.

## Variables

-   `password`: Almacena la contraseña ingresada por el usuario como una lista de caracteres.
-   `alfabeto`: Contiene todas las letras minúsculas del alfabeto.
-   `numeros`: Contiene los números del 0 al 9 (no utilizados actualmente en el código).
-   `seguir`: Variable booleana (no utilizada actualmente en el código).
-   `inicio`: Almacena el tiempo de inicio del ataque.
-   `intento`: Almacena la combinación de letras que se está probando en cada iteración.
-   `final`: Almacena el tiempo final cuando la contraseña es encontrada.

## Consideraciones

-   **Seguridad:** Este código es solo para fines educativos. Los ataques de fuerza bruta pueden ser muy lentos e ineficientes para contraseñas más largas o que incluyan diferentes tipos de caracteres.
-   **Optimización:** El código podría ser optimizado para manejar contraseñas con diferentes longitudes y conjuntos de caracteres.

## Ejemplo de Uso

1.  Ejecutar el script.
2.  Ingresar una contraseña de 4 letras minúsculas cuando se solicite.
3.  Presionar Enter para iniciar el ataque.
4.  Observar las combinaciones generadas en la consola.
5.  Si la contraseña es encontrada, se mostrará el mensaje "Clave encontrada" junto con el tiempo transcurrido.

	>Explicación: El algoritmo realiza una serie de validaciones, probando todas las claves hasta hallar la coincidencia. Al final revela la coincidencia y muestra el tiempo que le tomó en encontrarla.
  

        Ingrese una palabra clave de 4 letras: casa
		Presione Enter para continuar...
		a a a a
		...		
		c a r y
	    c a r z
	    c a s
	    c a s a
	    Clave encontrada:  ['c', 'a', 's', 'a']
		Tiempo consumido: 57.63 seg
