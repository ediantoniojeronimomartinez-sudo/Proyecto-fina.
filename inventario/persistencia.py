"""Lectura y escritura de información en archivos CSV."""

import csv
from pathlib import Path
from .modelos import Producto


class RepositorioCSV:
    """Gestiona el archivo CSV del inventario."""

    def __init__(self, ruta):
        self._ruta = Path(ruta)

    def cargar(self):
        """Carga los productos desde el archivo CSV."""
        productos = []
        self._ruta.parent.mkdir(parents=True, exist_ok=True)

        if not self._ruta.exists():
            return productos

        with self._ruta.open("r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                productos.append(
                    Producto(
                        fila["codigo"],
                        fila["nombre"],
                        fila["categoria"],
                        float(fila["precio"]),
                        int(fila["stock"])
                    )
                )
        return productos

    def guardar(self, productos):
        """Guarda todos los productos en el archivo CSV."""
        self._ruta.parent.mkdir(parents=True, exist_ok=True)

        with self._ruta.open("w", encoding="utf-8", newline="") as archivo:
            campos = ["codigo", "nombre", "categoria", "precio", "stock"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()

            for producto in productos:
                escritor.writerow({
                    "codigo": producto.codigo,
                    "nombre": producto.nombre,
                    "categoria": producto.categoria,
                    "precio": f"{producto.precio:.2f}",
                    "stock": producto.stock
                })


class Bitacora:
    """Registra las operaciones de venta en un archivo de texto."""

    def __init__(self, ruta):
        self._ruta = Path(ruta)

    def registrar(self, venta):
        """Agrega una venta al final de la bitácora."""
        self._ruta.parent.mkdir(parents=True, exist_ok=True)
        with self._ruta.open("a", encoding="utf-8") as archivo:
            archivo.write(
                f"{venta.fecha} | Venta | {venta.codigo_producto} | "
                f"{venta.cantidad} | Q{venta.total:.2f}\n"
            )
