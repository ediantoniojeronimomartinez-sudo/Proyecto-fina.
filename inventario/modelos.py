"""Clases que representan los datos principales del sistema."""

from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod

from .excepciones import CodigoInvalidoError, DatosInvalidosError


class Producto:
    """Representa un producto de la panadería."""

    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self):
        """Obtiene el código del producto."""
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        """Valida y asigna el código del producto."""
        valor = str(valor).strip().upper()
        if not valor or len(valor) < 3:
            raise CodigoInvalidoError("El código debe tener al menos 3 caracteres.")
        self._codigo = valor

    @property
    def nombre(self):
        """Obtiene el nombre del producto."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Valida y asigna el nombre del producto."""
        valor = str(valor).strip()
        if not valor:
            raise DatosInvalidosError("El nombre no puede estar vacío.")
        self._nombre = valor.title()

    @property
    def categoria(self):
        """Obtiene la categoría del producto."""
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        """Valida y asigna la categoría del producto."""
        valor = str(valor).strip()
        if not valor:
            raise DatosInvalidosError("La categoría no puede estar vacía.")
        self._categoria = valor.title()

    @property
    def precio(self):
        """Obtiene el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor):
        """Valida y asigna el precio."""
        try:
            valor = float(valor)
        except ValueError:
            raise DatosInvalidosError("El precio debe ser numérico.")
        if valor <= 0:
            raise DatosInvalidosError("El precio debe ser mayor que cero.")
        self._precio = valor

    @property
    def stock(self):
        """Obtiene el stock disponible."""
        return self._stock

    @stock.setter
    def stock(self, valor):
        """Valida y asigna el stock."""
        try:
            valor = int(valor)
        except ValueError:
            raise DatosInvalidosError("El stock debe ser entero.")
        if valor < 0:
            raise DatosInvalidosError("El stock no puede ser negativo.")
        self._stock = valor

    def disminuir_stock(self, cantidad):
        """Disminuye el stock del producto."""
        self.stock = self.stock - cantidad

    def __str__(self):
        """Devuelve una representación legible del producto."""
        return f"{self.codigo} - {self.nombre} - Q{self.precio:.2f} - Stock: {self.stock}"

    def __repr__(self):
        """Devuelve una representación técnica del producto."""
        return f"Producto('{self.codigo}', '{self.nombre}', '{self.categoria}', {self.precio}, {self.stock})"

    def __eq__(self, otro):
        """Compara productos por código."""
        if not isinstance(otro, Producto):
            return False
        return self.codigo == otro.codigo


@dataclass(frozen=True)
class Venta:
    """Representa una venta registrada de forma inmutable."""

    codigo_producto: str
    nombre_producto: str
    cantidad: int
    precio_unitario: float
    total: float
    fecha: str

    def __str__(self):
        """Devuelve una representación de la venta."""
        return f"{self.fecha} | {self.codigo_producto} | {self.nombre_producto} | {self.cantidad} | Q{self.total:.2f}"


class ReglaNegocio(ABC):
    """Clase abstracta para aplicar una regla especial de negocio."""

    def __init__(self, nombre):
        self._nombre = nombre

    @abstractmethod
    def aplicar(self, subtotal, cantidad):
        """Aplica la regla al subtotal de una venta."""


class DescuentoPorVolumen(ReglaNegocio):
    """Aplica descuento cuando se compran varias unidades."""

    def __init__(self):
        super().__init__("Descuento por volumen")

    def aplicar(self, subtotal, cantidad):
        """Calcula el total aplicando descuento por volumen."""
        if cantidad >= 12:
            return subtotal * 0.90
        if cantidad >= 6:
            return subtotal * 0.95
        return subtotal


class PrecioNormal(ReglaNegocio):
    """Mantiene el precio normal cuando no aplica descuento."""

    def __init__(self):
        super().__init__("Precio normal")

    def aplicar(self, subtotal, cantidad):
        """Devuelve el subtotal sin descuento."""
        return subtotal
