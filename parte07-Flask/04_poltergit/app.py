from flask import Flask, render_template, request
import pyautogui as auto  # CORRIGIDO: Adicionado 'as auto' para seus comandos funcionarem
from datetime import date

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# -------------------------------------------------------------------------

@app.route("/commitar", methods=['POST'])
def commitar():
    hoje = date.today().strftime("%d/%m/%Y")  # CORRIGIDO: strftime (com f)
    repositorio = None
    
    if request.method == "POST":
        repositorio = request.form.get("repositorio", "")
        
    if repositorio:
        auto.PAUSE = 1
        auto.hotkey("win", "r")
        auto.write("cmd")
        auto.press("enter")
        auto.sleep(1) 
        auto.write(f"cd {repositorio}")
        auto.press("enter")
        auto.write("git add .")
        auto.press("enter")
        auto.write(f'git commit -m "Commit do dia {hoje}, dor e sofrimento."')
        auto.press("enter")
        auto.write("git push")
        auto.press("enter")
        auto.sleep(3)
        auto.write("exit")
        auto.press("enter")
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
