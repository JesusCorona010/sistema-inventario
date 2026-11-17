"""Pruebas de la funcionalidad Producto: CP01 a CP07."""
import contextlib
import io
import unittest
from src.producto import Producto


class TestProducto(unittest.TestCase):
    def setUp(self):
        self.producto = Producto("P001", "Teclado", 350, 10)

    def salida(self, producto):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            producto.mostrar()
        return buffer.getvalue()

    def test_cp01_crear_producto(self):
        self.assertIsInstance(self.producto, Producto)
        self.assertEqual((self.producto.codigo, self.producto.nombre, self.producto.precio, self.producto.existencia), ("P001", "Teclado", 350, 10))

    def test_cp02_mostrar_codigo(self):
        self.assertIn("Código: P001", self.salida(self.producto))

    def test_cp03_mostrar_nombre(self):
        self.assertIn("Nombre: Teclado", self.salida(self.producto))

    def test_cp04_mostrar_precio(self):
        self.assertIn("Precio: $350.00", self.salida(self.producto))

    def test_cp05_mostrar_existencia(self):
        self.assertIn("Existencia: 10", self.salida(self.producto))

    def test_cp06_mostrar_informacion_completa(self):
        salida = self.salida(self.producto)
        for dato in ("Código: P001", "Nombre: Teclado", "Precio: $350.00", "Existencia: 10"):
            with self.subTest(dato=dato):
                self.assertIn(dato, salida)

    def test_cp07_crear_otro_producto(self):
        segundo = Producto("P002", "Mouse", 180, 5)
        self.assertEqual((segundo.codigo, segundo.nombre, segundo.precio, segundo.existencia), ("P002", "Mouse", 180, 5))
        self.assertIn("Nombre: Mouse", self.salida(segundo))
        self.assertIn("Nombre: Teclado", self.salida(self.producto))
        self.assertNotIn("Nombre: Mouse", self.salida(self.producto))


if __name__ == "__main__":
    unittest.main()
