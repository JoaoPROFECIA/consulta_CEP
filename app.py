from interface_grafica import *

tela_inicial()

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break
