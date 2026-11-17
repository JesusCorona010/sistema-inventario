# Procedimiento RELEASE

1. Verificar que TEST y BUILD terminen correctamente en main.
2. Confirmar que el workflow release.yml esté integrado a main.
3. Crear el tag v1.0.0 en el commit aprobado de main y enviarlo a GitHub.
4. El workflow valida sintaxis, ejecuta las siete pruebas, empaqueta src/ en sistema-inventario-v1.0.0.zip y publica GitHub Release.
5. Descargar el ZIP desde Releases, extraerlo y comprobar que contiene src/producto.py y src/busqueda.py.
6. Registrar URL de la ejecución, fecha, tag y resultado. Si falla la validación, no se publica el ZIP.

## Ejercicio de error

En una rama de ejercicio, introducir una modificación que rompa una prueba, verificar su detección y corregirla. La práctica también solicita demostrar un tag fallido v1.0.1 y una nueva versión corregida v1.0.2; no reutilizar tags. No etiquetar un commit defectuoso en main sin coordinación con el equipo.

## Reflexión

1. Las versiones permiten rastrear exactamente qué código se distribuye.
2. Commit: cambio registrado; tag: nombre de un commit; release: publicación con archivos.
3. Las pruebas impiden distribuir fallos conocidos.
4. Si fallan, el job se detiene antes de publicar.
5. El paquete automático evita omisiones y mejora la reproducibilidad.
6. El historial documenta cambios y facilita regresar a versiones previas.
7. Release publica un paquete; deploy lo instala o ejecuta en un entorno.
