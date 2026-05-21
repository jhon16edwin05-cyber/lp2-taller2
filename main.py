from flask import Flask, render_template, redirect
import sqlite3

# cargamos todos los datos desde la DB en una función
def cargar_productos(db_path="web2.sqlite3"):
  conexion = sqlite3.connect(db_path)
  conexion.row_factory = sqlite3.Row
  cursor = conexion.cursor()
  cursor.execute("SELECT * FROM products;")
  productos = [dict(producto) for producto in cursor.fetchall()]
  cursor.close()
  conexion.close()
  return productos

productos = cargar_productos()

# aplicación
app = Flask(__name__)


# rutas
@app.route('/')
def ruta_raiz():
  return render_template("index.html", productos=productos)


@app.route('/producto/<int:pid>')
def ruta_producto(pid):
  for producto in productos:
    if pid == producto["id"]:
      return render_template("producto.html", producto=producto)
  return redirect("/")


# programa principal
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

