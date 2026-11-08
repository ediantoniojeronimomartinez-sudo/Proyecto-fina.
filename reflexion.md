# Reflexión

La versión final del proyecto transforma el sistema inicial de inventario y ventas en una estructura orientada a objetos. Antes, las operaciones podían concentrarse en funciones y datos separados; ahora cada clase tiene una responsabilidad definida.

Una de las principales ventajas de POO fue poder separar el producto, inventario, ventas, archivos, reportes y reglas de negocio. Esto hace que sea más sencillo localizar una parte del programa cuando se necesita modificarla.

El encapsulamiento se utilizó especialmente en la clase `Producto`, donde precio, stock y código se validan mediante propiedades. La herencia se utilizó con `ReglaNegocio`, que es abstracta, y sus clases concretas. El polimorfismo permite que el sistema trabaje con una regla mediante el mismo método `aplicar()`.

La parte más complicada fue organizar el proyecto sin perder las funciones principales del sistema. Se resolvió separando las responsabilidades en módulos y probando cada operación desde el menú.

Para realizar el proyecto se utilizaron materiales de clase sobre UML, programación orientada a objetos, cadenas, archivos, colecciones y modularización, además de herramientas de apoyo para revisar y estructurar parte del código. El código debe ser comprendido y puede ser modificado durante la defensa.
