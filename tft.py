from python_imagesearch.imagesearch import imagesearch
import pyautogui
import time

def search(img):
    return img[0] != -1

def dar_queue():
    pyautogui.moveTo(queue[0], queue[1])
    pyautogui.click()
    time.sleep(1)

def aceitar_partida():
    pyautogui.moveTo(aceitar[0], aceitar[1])
    pyautogui.click()

def reconectar_partida():
    pyautogui.moveTo(reconectar[0], reconectar[1])
    pyautogui.click()

def quitar(partida):
    engrenagem = imagesearch("./captures/engrenagem.png")
    pyautogui.moveTo(engrenagem[0], engrenagem[1])
    pyautogui.mouseDown(); pyautogui.mouseUp()
    time.sleep(4)
    render = imagesearch("./captures/render-se.png")
    pyautogui.moveTo(render[0], render[1])
    pyautogui.mouseDown(); pyautogui.mouseUp()
    time.sleep(4)
    render_2 = imagesearch("./captures/render-se-2.png")
    pyautogui.moveTo(render_2[0], render_2[1])
    pyautogui.mouseDown(); pyautogui.mouseUp()
    time.sleep(4)
    print("Partida "+str(partida)+" encerrada")

def queue_novamente():
    pyautogui.moveTo(jogar_novamente[0], jogar_novamente[1])
    pyautogui.click()
    time.sleep(1)

partida = 0
while True:
    queue = imagesearch("./captures/queue.png")
    aceitar = imagesearch("./captures/aceitar.png")
    reconectar = imagesearch("./captures/reconectar.png")
    hora_de_quitar = imagesearch("./captures/3-4.png")
    jogar_novamente = imagesearch("./captures/jogar-novamente.png")

    if search(queue):
        dar_queue()
    elif search(aceitar):
       aceitar_partida()
    elif search(reconectar):
        reconectar_partida()
    elif search(hora_de_quitar):
        partida +=1
        quitar(partida)
    elif search(jogar_novamente):
        queue_novamente() 