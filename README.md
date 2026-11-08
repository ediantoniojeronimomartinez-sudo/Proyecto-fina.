# Proyecto Final - Sistema de Inventario y Ventas de Panadería

**Estudiante:** Edi Antonio Jerónimo Martínez  
**Carné:** 7691 26 97  
**Curso:** Programación / Proyecto Final  
**Ciclo:** 2-2026  
**Tema:** Panadería

## Descripción

Sistema de consola desarrollado en Python para controlar productos, existencias y ventas de una panadería. El proyecto está organizado con Programación Orientada a Objetos y conserva el uso de cadenas, archivos CSV, colecciones y modularización.

## Regla especial

Se utiliza un descuento por volumen:

- De 1 a 5 unidades: precio normal.
- De 6 a 11 unidades: 5% de descuento.
- Desde 12 unidades: 10% de descuento.

Ejemplo: si una venta de 6 unidades tiene un subtotal de Q60.00, el total es Q57.00.

## Ejecución

Desde la carpeta raíz:

```text
python main.py
```

No se necesitan librerías externas.

## Clases principales

- `Producto`: datos y validaciones de los productos.
- `Venta`: representa una venta inmutable.
- `Inventario`: administra productos y ventas.
- `RepositorioCSV`: carga y guarda el inventario.
- `Bitacora`: registra las ventas con fecha y hora.
- `ReporteVentas`: presenta el reporte.
- `ReglaNegocio`: clase abstracta.
- `DescuentoPorVolumen` y `PrecioNormal`: implementaciones concretas.
- `SistemaInventario`: coordina la aplicación.
- Excepciones propias para errores del sistema.

## Estructura

```text
Proyecto_Panaderia_POO/
├── main.py
├── inventario/
│   ├── __init__.py
│   ├── app.py
│   ├── excepciones.py
│   ├── inventario.py
│   ├── modelos.py
│   ├── persistencia.py
│   ├── reglas.py
│   └── reportes.py
├── datos/
│   ├── inventario.csv
│   └── ventas.log
├── docs/
├── evidencias/
└── README.md
```

## Uso básico

1. Ejecutar `python main.py`.
2. Agregar o buscar productos.
3. Registrar ventas indicando código y cantidad.
4. Consultar el inventario ordenado por nombre o precio.
5. Consultar el reporte de ventas.
6. Seleccionar guardar y salir para conservar los cambios.

## Reflexión

El proyecto aplica encapsulamiento mediante propiedades, herencia mediante una clase abstracta de reglas, polimorfismo mediante el método `aplicar`, composición entre las partes del sistema y manejo de excepciones para evitar que los errores terminen en un traceback para el usuario.
