
from flask import Flask, render_template, redirect
from flask import Flask, render_template, redirect  # type: ignore
import sqlite3
from pprint import pprint

# cargamos todos los datos

conexion = sqlite3.connect("web2.sqlite3")
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()
cursor.execute("SELECT * FROM products;")
productos = [dict(producto) for producto in cursor.fetchall()]
cursor.close()
conexion.close()

# aplicación
app = Flask(__name__)


# rutas
@app.route('/')
@app.route("/")
def ruta_raiz():
  pass
  return render_template("index.html", productos=productos)


@app.route('/producto/<int:pid>')
@app.route("/producto/<int:pid>")
def ruta_producto(pid):
  pass
  
  for producto in productos:
        if pid == producto["id"]:
            return render_template("producto.html", producto=producto)
  return redirect("/")


# programa principal
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)