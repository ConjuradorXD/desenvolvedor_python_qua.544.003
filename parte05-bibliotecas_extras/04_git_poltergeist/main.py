import pyautogui as auto
from datetime import date

def hoje():
    return date.today().strftime("%d/%m/%Y")

def main():
    auto.PAUSE = 0.75

    auto.press("win")
    auto.write("cmd")
    auto.press("enter")
    auto.write(r'cd "C:\Users\ALUNO\Documents\Wallace vinicius\desenvolvedor_python_qua.544.003-main"')
    auto.press("enter")
    auto.write("git add .")
    auto.press("enter")
    auto.write(f'git commit -m "Dor e sofrimento na aula do dia {hoje()}."')
    auto.press("enter")
    auto.write("git push")
    auto.press("enter")
    auto.write("exit")
    auto.press("enter")
    


if __name__ == "__main__":
    main()
