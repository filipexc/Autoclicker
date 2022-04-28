import PySimpleGUI as sg
import time
import threading
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Controller , Button
class TelaPython:
    def __init__(self):
        #layout
        sg.theme("Reddit")
        layout = [
            [sg.Text('Tecla de Atalho',size= (15,0)),sg.Input(size=(4,0),key='atalho',)],
            [sg.Text('Intervalo entre clicks')],
            [sg.Slider(range=(0.0001,1), key='Velocidade',default_value= (0.0001),orientation= 'h',size =(40,20),resolution= (0.0001))],
            [sg.Button('Confirmar')],
            [sg.Output(size=(30,20))],
        ]
        #janela
        self.janela = sg.Window('AutoClicker By Filipe Pereira').layout(layout)



    def iniciar(self):
        while True:
            #extrair dados
            self.button, self.values = self.janela.Read()
            global tecla_atalho
            tecla_atalho = self.values['atalho']
            global intervalo
            intervalo = self.values['Velocidade']
            print(f'{tecla_atalho} , {intervalo}')
            print(f'Tecla de atalho: {tecla_atalho}')
            print(f'intervalo de clicks: {intervalo}')
            
            Toggle_key = KeyCode(char= 't')
            print(Toggle_key)
            clicking = False
            mouse = Controller()

            def clicker():
                while True:
                    if clicking:
                        mouse.click(Button.left , 1)
                    time.sleep(0.0001)
                
            def toggle_event(key):
                if key == Toggle_key:
                    global clicking
                    clicking = not clicking


            click_thread = threading.Thread(target= clicker)
            click_thread.start()

            with Listener(on_press= toggle_event) as listener:
                listener.join()


    def atualiza(self):
        tecla_at = tecla_atalho
        return tecla_at



""""
            Toggle_key = KeyCode(char= self.tecla_atalho)
            print(Toggle_key)
            clicking = False
            mouse = Controller()

            def clicker():
                while True:
                    if clicking:
                        mouse.click(Button.left , 1)
                    time.sleep(0.0001)
                
            def toggle_event(key):
                if key == Toggle_key:
                    global clicking
                    clicking = not clicking


            click_thread = threading.Thread(target= clicker)
            click_thread.start()

            with Listener(on_press= toggle_event) as listener:
                listener.join() """
