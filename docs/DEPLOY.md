# Procedimiento DEPLOY

## Requisitos

- Versión publicada en GitHub Releases (por ejemplo, v1.0.0).
- Python 3.12 o compatible y unzip para despliegue local.
- No requiere dependencias externas, base de datos ni variables secretas para la funcionalidad actual.

## Despliegue manual

1. Descargar sistema-inventario-v1.0.0.zip desde GitHub Releases.
2. Extraer en una carpeta vacía de despliegue.
3. Ejecutar `python src/producto.py` y `python src/busqueda.py` desde la carpeta extraída.
4. Verificar que los productos se muestran con código, nombre, precio y existencia y que la búsqueda funciona.

## Despliegue automatizado

En Actions, ejecutar manualmente `DEPLOY - Verificar artefacto liberado` con la versión deseada. El workflow descarga el ZIP **ya publicado**, lo extrae en el runner Ubuntu, ejecuta los dos programas y guarda evidencia. El runner es temporal: no es un servidor permanente. Para desplegar en un servidor real se requiere un destino SSH y secretos DEPLOY_HOST, DEPLOY_USER, DEPLOY_KEY y DEPLOY_PORT; no se han configurado ni se supone su existencia.

## Diagnóstico

- Release inexistente: confirmar tag y ZIP publicado.
- Python no encontrado: instalar Python y verificar PATH.
- ZIP incompleto: revisar el workflow RELEASE y el contenido publicado.
- Fallo al ejecutar: consultar los logs y regresar al ZIP anterior estable.

## Recuperación (rollback)

Conservar el ZIP de cada versión. Para regresar a v1.0.0 después de desplegar una versión posterior, seleccionar v1.0.0 en el workflow DEPLOY o descargar y extraer su ZIP en una carpeta limpia, ejecutar y verificar de nuevo. El ejercicio completo requiere disponer de dos versiones reales y registrar ambas ejecuciones.

## Reflexión

1. Release publica; deploy instala y ejecuta.
2. Usar el paquete liberado garantiza la misma versión validada.
3. El destino proporciona el entorno de ejecución.
4. SSH necesita host, usuario, puerto y credenciales seguras.
5. Los secretos evitan exponer credenciales en YAML.
6. Automatizar hace el procedimiento repetible y auditable.
7. Versiones incompatibles o herramientas ausentes pueden impedir el inicio.
8. El rollback permite restaurar una versión estable.
