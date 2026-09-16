from flask import Flask, render_template, request
import pyautogui

app = Flask(__name__)

@app.route("/commitar",methods = ['POST'])
def commitar():
    hoje = date.today().srftime("%d/%m/%Y")
    msg = None
    repositorio = None
    if request.method == "POST":
        repositorio = request.form.get("repositorio","")
    if repositorio:
        auto.PAUSE = 1
        auto.hotkey("win","r")
        auto.write("cmd")
        auto.press("enter")
        auto.white(f"cd {repositorio}")
        auto.press("enter")
    else:
        msg = "Repositorio Inválido."
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)