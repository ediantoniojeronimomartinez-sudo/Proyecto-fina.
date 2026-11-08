"""Excepciones propias del sistema."""

class InventarioError(Exception):
    """Excepción base del sistema de inventario."""


class ProductoNoEncontradoError(InventarioError):
    """Se produce cuando no existe el producto solicitado."""


class StockInsuficienteError(InventarioError):
    """Se produce cuando no hay suficiente existencia para una venta."""


class CodigoInvalidoError(InventarioError):
    """Se produce cuando el código de un producto no es válido."""


class DatosInvalidosError(InventarioError):
    """Se produce cuando un dato no cumple las reglas del sistema."""
