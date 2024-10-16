from flask import Flask,render_template,request

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quienes-somos")
def quienes_somos():
    return render_template("quienes_somos.html")

# Ruta para la página de servicios
@app.route("/servicios")
def servicios():
    return render_template("servicios.html")


@app.route("/noticias")
def noticias():
    return render_template("noticias.html")



# Ruta para la página de contacto
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)
