# Evidencias y procedimiento TEST

Proyecto: sistema-inventario (Python 3.12). Herramienta: unittest.

## Casos de prueba

| ID | Entrada | Resultado esperado |
| --- | --- | --- |
| CP01 | P001, Teclado, 350, 10 | Producto creado con cuatro atributos |
| CP02 | P001 | Código: P001 |
| CP03 | Teclado | Nombre: Teclado |
| CP04 | 350 | Precio: $350.00 |
| CP05 | 10 | Existencia: 10 |
| CP06 | P001, Teclado, 350, 10 | Los cuatro campos aparecen |
| CP07 | P002, Mouse, 180, 5 | Segundo producto independiente |

## Ejecución

```bash
python -m unittest discover -s tests -v
```

Guardar como evidencia el registro real de GitHub Actions en el workflow TEST.

## Error detectado en el código original

Antes de la corrección, el método `Producto.mostrar()` imprimía `Número de whahtsaap waza` en lugar de `Existencia`. Los casos CP05 y CP06 están diseñados para detectar esa diferencia. Se corrigió la etiqueta sin cambiar el valor del atributo. Para documentar una falla real, consultar la ejecución fallida del workflow de la rama antes de corregirla; no presentar resultados simulados como evidencia.

## Reflexión

1. Las pruebas evitan incorporar regresiones a la rama principal.
2. Un caso define entrada y resultado esperado; la prueba automatizada lo verifica ejecutando código.
3. El resultado esperado es el requisito; el obtenido es lo que produjo la ejecución.
4. Una modificación incorrecta provoca el fallo de las aserciones afectadas.
5. GitHub Actions ejecuta las pruebas en un entorno repetible y deja registros.
6. Repetir pruebas después de cambios permite detectar regresiones.

## BUILD

El workflow `build.yml` prepara Python 3.12, comprueba la sintaxis con `compileall` y ejecuta las pruebas. Python no requiere compilar un ejecutable para este proyecto. Un error de sintaxis causa una ejecución fallida; al corregirlo, el workflow debe volver a ejecutarse. Fuentes: https://docs.github.com/actions y https://docs.python.org/3/library/compileall.html.

Preguntas BUILD: (1) Evita integrar código que no se puede ejecutar. (2) Actions comprueba cada cambio automáticamente en un runner. (3) Un error de sintaxis detiene el paso de compilación. (4) Detectarlo pronto reduce el costo de corregirlo.
