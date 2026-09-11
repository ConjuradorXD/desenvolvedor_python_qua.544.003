from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/imc", methods = ['GET','POST'])
def calcular_imc():
    if request.method == "POST":
        nome = request.form.get("nome","")
        massa = request.form.get("massa","")
        altura = request.form.get("altura","")
        imc = massa/(altura**2)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)