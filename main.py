import time
import threading
from more_itertools import interleave_longest
from numpy import character
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Controller , Button
import gooeypie as gp

app = gp.GooeyPieApp('AutoClicker By Filipe Pereira')
app.width = 500

#funcao para mudar a variavel atalho
def change_tk(event):
    global Toggle_key
    Toggle_key = charclick.text
    confirm_lbl.text = 'Atalho escolhido com sucesso'
    print(Toggle_key)
    return Toggle_key

#lógica para o autoclicker
def call_listener(event):
    with Listener(on_press= toggle_event) as listener:
        listener.join()
""" def mudar_intervalo(event):
    global interlo 
    intervalo = 0 """
def clicker():
    while True:
        if clicking:
            mouse.click(Button.left , 1)
        time.sleep(0.0001)
    
def toggle_event(key):
    if key == KeyCode(char= Toggle_key):
        global clicking
        print(f'changetk e {Toggle_key}')
        clicking = not clicking

#criando o layout
confirm_btn = gp.Button(app , 'Confirmar atalho', change_tk)
confirm_btn2 = gp.Button(app , 'Rodar', call_listener)
confirm_lbl = gp.Label(app, '')
charclick = gp.Input(app)


input_text = gp.Label(app,'Digite o atalho no campo ao lado')

#criando grid e incluindo os widgets na window app
app.set_grid(3, 3)

app.add(confirm_btn, 1, 3 , align='center',)
app.add(charclick, 1, 2,align = 'center')
app.add(input_text,1,1,align = 'center')
app.add(confirm_lbl, 2, 1 , align='center')
app.add(confirm_btn2,3,3, align = 'center')



#lógica para o autoclicker
clicking = False
mouse = Controller()


click_thread = threading.Thread(target= clicker)
click_thread.start()
app.run()

   
