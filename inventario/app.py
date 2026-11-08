"""Interfaz principal del sistema."""

from pathlib import Path

from .inventario import Inventario
from .persistencia import RepositorioCSV, Bitacora
from .reportes import ReporteVentas
from .modelos import DescuentoPorVolumen
from .excepciones import InventarioError, DatosInvalidosError


class SistemaInventario:
    """Coordina el menú, inventario, persistencia y reglas de negocio."""

    def __init__(self):
        base = Path(__file__).resolve().parent.parent
        self._inventario = Inventario()
        self._repositorio = RepositorioCSV(base / "datos" / "inventario.csv")
        self._bitacora = Bitacora(base / "datos" / "ventas.log")
        self._regla = DescuentoPorVolumen()
        self._cargar_datos()

    def _cargar_datos(self):
        """Carga los productos almacenados."""
        for producto in self._repositorio.cargar():
            self._inventario.agregar_producto(producto)

    def _guardar_datos(self):
        """Guarda los cambios del inventario."""
        productos = self._inventario.productos_ordenados(1)
        self._repositorio.guardar(productos)

    def ejecutar(self):
        """Ejecuta el menú principal."""
        while True:
            self._mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            try:
                if opcion == "1":
                    self._agregar_producto()
                elif opcion == "2":
                    self._buscar_producto()
                elif opcion == "3":
                    self._registrar_venta()
                elif opcion == "4":
                    self._mostrar_inventario()
                elif opcion == "5":
                    ReporteVentas.mostrar(self._inventario.reporte_ventas())
                elif opcion == "6":
                    self._guardar_datos()
                    print("Cambios guardados. Hasta luego.")
                    break
                else:
                    print("Opción no válida.")
            except InventarioError as error:
                print(f"Error: {error}")
            except (ValueError, KeyError) as error:
                print(f"Error en los datos ingresados: {error}")

    @staticmethod
    def _mostrar_menu():
        """Muestra las opciones del sistema."""
        print("\n" + "=" * 50)
        print("      PANADERÍA - INVENTARIO Y VENTAS")
        print("=" * 50)
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Registrar venta")
        print("4. Mostrar inventario")
        print("5. Reporte de ventas")
        print("6. Guardar y salir")
        print("=" * 50)

    def _agregar_producto(self):
        """Solicita los datos y agrega un producto."""
        from .modelos import Producto

        codigo = input("Código: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = input("Precio: ")
        stock = input("Stock: ")

        producto = Producto(codigo, nombre, categoria, precio, stock)
        self._inventario.agregar_producto(producto)
        self._guardar_datos()
        print("Producto agregado correctamente.")

    def _buscar_producto(self):
        """Busca y muestra productos."""
        texto = input("Código o parte del nombre: ")
        resultados = self._inventario.buscar(texto)

        if not resultados:
            print("No se encontraron productos.")
            return

        for producto in resultados:
            print(f"{producto.codigo:<8} {producto.nombre:<25} "
                  f"Q{producto.precio:>8.2f}  Stock: {producto.stock}")

    def _registrar_venta(self):
        """Solicita datos y registra una venta."""
        codigo = input("Código del producto: ")
        cantidad = int(input("Cantidad: "))

        venta = self._inventario.registrar_venta(
            codigo, cantidad, self._regla
        )
        self._bitacora.registrar(venta)
        self._guardar_datos()

        print(f"Venta registrada. Total: Q{venta.total:.2f}")

    def _mostrar_inventario(self):
        """Muestra el inventario ordenado."""
        print("\n1. Ordenar por nombre")
        print("2. Ordenar por precio")
        criterio = input("Seleccione criterio: ").strip()

        if criterio not in ("1", "2"):
            raise DatosInvalidosError("Criterio de ordenamiento no válido.")

        productos = self._inventario.productos_ordenados(int(criterio))

        print("\n" + "=" * 65)
        print(f"{'CODIGO':<10}{'PRODUCTO':<25}{'CATEGORIA':<15}{'PRECIO':>8}")
        print("-" * 65)

        for producto in productos:
            print(
                f"{producto.codigo:<10}"
                f"{producto.nombre[:24]:<25}"
                f"{producto.categoria[:14]:<15}"
                f"Q{producto.precio:>7.2f}"
            )
        print("=" * 65)
