import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from helper.lang import LANGUAGES

translator = Translator()

def clear():
    T2.delete(1.0, "end-1c")

def translate(source='id',dest='id'):
    clear()
    try:
        translation = translator.translate(T1.get(1.0, "end-1c"), source=source,dest=dest)
        T2.insert(tk.END, translation.text)
    except Exception as err:
        raise 


root = tk.Tk()
root.title("Translate")
root.geometry("500x250")

var = dict()
var['source'] = tk.StringVar()
var['destiny'] = tk.StringVar()

comboSource = ttk.Combobox(
    root, 
    values=list(LANGUAGES.keys()), 
    justify="center", 
    textvariable=var['source'],
    state="readonly",
)

comboDestiny = ttk.Combobox(
    root, 
    values=list(LANGUAGES.keys()), 
    justify="center", 
    textvariable=var['destiny'],
    state="readonly",
)

comboSource.current(0)
comboDestiny.current(0)

T1 = tk.Text(root, height=5, width=250)
T2 = tk.Text(root, height=5, width=250)
b = tk.Button(root, text='Translate', command= lambda: translate(LANGUAGES[var['source'].get()],LANGUAGES[var['destiny'].get()]))

comboSource.pack() #fix?
T1.pack()
comboDestiny.pack() #fix?
T2.pack()
b.pack()

root.mainloop()
