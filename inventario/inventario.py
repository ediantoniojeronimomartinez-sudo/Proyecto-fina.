"""Administración del inventario y las ventas."""

from datetime import datetime
from .modelos import Producto, Venta
from .excepciones import ProductoNoEncontradoError, StockInsuficienteError, DatosInvalidosError


class Inventario:
    """Contiene productos y registra las ventas de la panadería."""

    def __init__(self):
        self._productos = {}
        self._categorias = set()
        self._ventas = []

    def agregar_producto(self, producto):
        """Agrega un producto al inventario."""
        if not isinstance(producto, Producto):
            raise DatosInvalidosError("El objeto no es un producto válido.")
        self._productos[producto.codigo] = producto
        self._categorias.add(producto.categoria)

    def buscar(self, texto):
        """Busca productos por código o por parte del nombre."""
        texto = str(texto).strip().lower()
        return [
            producto for producto in self._productos.values()
            if texto in producto.codigo.lower() or texto in producto.nombre.lower()
        ]

    def obtener_producto(self, codigo):
        """Obtiene un producto mediante su código."""
        codigo = str(codigo).strip().upper()
        if codigo not in self._productos:
            raise ProductoNoEncontradoError("No se encontró el producto.")
        return self._productos[codigo]

    def registrar_venta(self, codigo, cantidad, regla):
        """Registra una venta después de validar el stock."""
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise DatosInvalidosError("La cantidad debe ser mayor que cero.")

        producto = self.obtener_producto(codigo)

        if cantidad > producto.stock:
            raise StockInsuficienteError(
                f"Stock insuficiente. Disponible: {producto.stock}."
            )

        subtotal = producto.precio * cantidad
        total = regla.aplicar(subtotal, cantidad)
        producto.disminuir_stock(cantidad)

        venta = Venta(
            producto.codigo,
            producto.nombre,
            cantidad,
            producto.precio,
            total,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self._ventas.append(venta)
        return venta

    def productos_ordenados(self, criterio=1):
        """Devuelve productos ordenados por nombre o precio."""
        if criterio == 1:
            return sorted(self._productos.values(), key=lambda p: p.nombre.lower())
        return sorted(self._productos.values(), key=lambda p: p.precio)

    def reporte_ventas(self):
        """Devuelve las ventas registradas."""
        return tuple(self._ventas)

    def categorias(self):
        """Devuelve las categorías existentes."""
        return set(self._categorias)

    def __len__(self):
        """Devuelve la cantidad de productos."""
        return len(self._productos)

    def __contains__(self, codigo):
        """Indica si un código existe en el inventario."""
        return str(codigo).strip().upper() in self._productos
