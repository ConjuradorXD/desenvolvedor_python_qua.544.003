
import pyautogui as auto
import time

def ir_pesquisa():
    auto.press("tab")
    auto.press("tab")
    auto.press("tab")
    auto.press("tab")


def main ():
    auto.PAUSE = 0.75
    auto.press("win")
    auto.write("firefox")
    auto.press("enter")
    auto.write("youtube.com.br")
    auto.press("enter")
    time.sleep(3)
    ir_pesquisa()
    auto.write("youtube.com.br")


if __name__ == "__main__":
    main()

