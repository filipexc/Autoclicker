import time
import threading
from numpy import character
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Controller , Button
import gooeypie as gp

app = gp.GooeyPieApp('AutoClicker By Filipe Pereira')
app.width = 500
def change_tk(event):
    global Toggle_key
    Toggle_key = charclick.text
    confirm_lbl.text = 'Foi'
    print(Toggle_key)
    return Toggle_key

def call_listener(event):
    with Listener(on_press= toggle_event) as listener:
        listener.join()
    

confirm_btn = gp.Button(app , 'Confirmar atalho', change_tk)
confirm_btn2 = gp.Button(app , 'Rodar', call_listener)
confirm_lbl = gp.Label(app, '')
text_lbl= gp.Label(app,'By Filipe Pereira')
charclick = gp.Input(app)

app.set_grid(3, 2)
app.add(confirm_btn, 1, 2 , align='center',)
app.add(confirm_lbl, 2, 1 , align='center')
app.add(charclick, 1, 1,align = 'center')
app.add(confirm_btn2,3,2, align = 'center')
app.add(text_lbl,3,1)



clicking = False
mouse = Controller()

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


click_thread = threading.Thread(target= clicker)
click_thread.start()
app.run()

   
