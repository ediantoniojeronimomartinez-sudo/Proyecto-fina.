from inventario.inventario import Inventario
from inventario.modelos import Producto, DescuentoPorVolumen

inventario = Inventario()
inventario.agregar_producto(Producto("TST001", "Pan de Prueba", "Panadería", 10, 20))
venta = inventario.registrar_venta("TST001", 6, DescuentoPorVolumen())
print(f"Total de prueba: Q{venta.total:.2f}")
print(f"Stock restante: {inventario.obtener_producto('TST001').stock}")
