import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
import script1
def script(): script1.metod()

window = Tk()
window.title('SchoolScan')
window.geometry('1280x760')
window['bg'] = 'grey'
window.wm_attributes('-alpha', 1)

frame = Frame(
    window,
    padx=3,
    pady=3
)
frame.pack(expand=True)

def notReady():
    script()

start_text = Label(
    frame,
    text='''Здравствуйте! 
    Мы вас приветствуем в приложении SchoolScan! 
    Это приложение предназначено для самоконтроля детей и их мотвации к учёбе. 
    Пользуйтесь им грамотно, при ошибках сразу сообщайте :)''',
)
start_text.grid(row=2, column=1)
start_btn = Button(
    frame,
    text='Поехали!',
    command=notReady
)
start_btn.grid(row=6, column=1)
mainloop()
