"""Generación de reportes de ventas."""

class ReporteVentas:
    """Presenta las ventas en columnas alineadas."""

    @staticmethod
    def mostrar(ventas):
        """Muestra las ventas con formato de tabla."""
        print("\n" + "=" * 78)
        print("REPORTE DE VENTAS")
        print("=" * 78)
        print(f"{'FECHA':<20}{'CODIGO':<10}{'PRODUCTO':<24}{'CANT.':>7}{'TOTAL':>12}")
        print("-" * 78)

        if not ventas:
            print("No hay ventas registradas.")
        else:
            for venta in ventas:
                print(
                    f"{venta.fecha:<20}"
                    f"{venta.codigo_producto:<10}"
                    f"{venta.nombre_producto[:23]:<24}"
                    f"{venta.cantidad:>7}"
                    f"Q{venta.total:>10.2f}"
                )

        print("=" * 78)
