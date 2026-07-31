
## Descripción del Proyecto

El programa solicita al usuario la longitud de los tres lados de un triángulo ($A$, $B$ y $C$) y realiza las siguientes validaciones y clasificaciones:

- **Validación del Triángulo:** Comprueba la condición de que la suma de dos lados siempre sea mayor que el tercer lado:
- **Equilátero:** Los 3 lados son exactamente iguales.
- **Isósceles:** Tiene 2 lados iguales y 1 diferente.
- **Escaleno:** Los 3 lados tienen longitudes distintas.

---

## Requisitos del Sistema

Para ejecutar esta aplicación, tu computadora requiere:

- **Sistema Operativo:** Windows 7 o superior, macOS 10.12 o superior, o Linux (Ubuntu, Debian, Fedora, etc.).
- **Procesador:** Cualquier procesador moderno (x86, x64 o ARM).
- **Memoria RAM:** Mínimo 512 MB (requiere muy pocos recursos).
- **Espacio en Disco:** Menos de 10 MB libres.

---

## Instalación y Librerías

### Requisito Principal: Python
El programa está escrito en **Python 3**. No requiere la instalación de librerías externas o de terceros.

- **Versión de Python recomendada:** Python 3.6 o superior.
- **Descarga:** [python.org/downloads](https://www.python.org/downloads/)

---

## Cómo Ejecutar el Programa

### Paso 1: Clonar o descargar el código
Guarda el código fuente en un archivo llamado `verificador_triangulos.py`.

### Paso 2: Abrir la Terminal o Consola de Comandos
- **Windows:** Presiona `Win + R`, escribe `cmd` o `powershell` y presiona *Enter*.
- **macOS / Linux:** Abre la aplicación **Terminal**.

### Paso 3: Navegar hasta la carpeta del archivo
Escribe el comando `cd` seguido de la ruta donde guardaste el archivo:

### Paso 4: Ejecutar la aplicación
Ejecuta el script corriendo el siguiente comando:

- En **Windows**:
  ```bash
  python verificador_triangulos.py
  ```
- En **macOS / Linux**:
  ```bash
  python3 verificador_triangulos.py
  ```

---

## Ejemplos de Uso

### Ejemplo 1: Triángulo Equilátero
```text
Ingrese el lado A del triangulo: 5
Ingrese el lado B del triangulo: 5
Ingrese el lado C del triangulo: 5
Resultado: El triángulo es Equilátero.
```

### Ejemplo 2: Triángulo Isósceles
```text
Ingrese el lado A del triangulo: 6
Ingrese el lado B del triangulo: 6
Ingrese el lado C del triangulo: 4
Resultado: El triángulo es Isósceles.
```

### Ejemplo 3: Triángulo Escaleno
```text
Ingrese el lado A del triangulo: 3
Ingrese el lado B del triangulo: 4
Ingrese el lado C del triangulo: 5
Resultado: El triángulo es Escaleno.
```

### Ejemplo 4: Valores no válidos (No forman triángulo)
```text
Ingrese el lado A del triangulo: 1
Ingrese el lado B del triangulo: 2
Ingrese el lado C del triangulo: 10
Los valores ingresados no forman un triángulo.
